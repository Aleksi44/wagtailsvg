from wagtail.core.widget_adapters import WidgetAdapter
from wagtail.core.telepath import register
from wagtailsvg.models import Svg
import json
from django.contrib.admin.utils import quote
from django.forms import widgets
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from wagtail.utils.widgets import WidgetWithScript


class AdminSvgChooser(WidgetWithScript, widgets.Input):
    choose_one_text = _("Choose a SVG item")
    choose_another_text = _("Choose another SVG item")
    link_to_chosen_text = _("Edit this SVG item")
    model = Svg
    choose_modal_url_name = 'svg_chooser:choose'
    edit_item_url_name = 'wagtailsvg_svg_modeladmin_edit'
    input_type = 'hidden'
    clear_choice_text = _("Clear choice")
    show_edit_link = True
    classname = None  # CSS class for the top-level element
    template = "generic_chooser/widgets/chooser.html"
    is_hidden = False

    def get_instance(self, value):
        return self.model.objects.get(pk=value)

    def get_edit_item_url(self, instance):
        if self.edit_item_url_name is None:
            return None
        else:
            return reverse(self.edit_item_url_name, args=(quote(instance.pk),))

    def get_choose_modal_url(self):
        if self.choose_modal_url_name is None:
            return None
        else:
            return reverse(self.choose_modal_url_name)

    def value_from_datadict(self, data, files, name):
        # treat the empty string as None
        result = super().value_from_datadict(data, files, name)
        if result == '':
            return None
        else:
            return result

    def get_title(self, instance):
        return str(instance)

    def get_value_data(self, value):
        if value is None:
            return None
        elif isinstance(value, self.model):
            image = value
        else:  # assume image ID
            image = self.model.objects.get(pk=value)

        return {
            'id': image.pk,
            'title': image.title,
            'preview_url': image.url,
            'edit_url': reverse(
                'wagtailsvg_svg_modeladmin_edit',
                args=[image.id]
            ),
        }

    def render_html(self, name, value_data, attrs):
        value_data = value_data or {}
        original_field_html = super().render_html(
            name,
            value_data.get('id'),
            attrs
        )

        return render_to_string(self.template, {
            'widget': self,
            'original_field_html': original_field_html,
            'attrs': attrs,
            'value': bool(value_data),
            'title': value_data.get('title', ''),
            'preview_url': value_data.get('preview_url', {}),
            'edit_url': value_data.get('edit_url', ''),
        })

    def render_js_init(self, id_, name, value):
        return "createChooserWidget({0});".format(json.dumps(id_))

    def __init__(self, **kwargs):
        # allow choose_one_text / choose_another_text
        # to be overridden per-instance
        if 'choose_one_text' in kwargs:
            self.choose_one_text = kwargs.pop('choose_one_text')
        if 'choose_another_text' in kwargs:
            self.choose_another_text = kwargs.pop('choose_another_text')
        if 'clear_choice_text' in kwargs:
            self.clear_choice_text = kwargs.pop('clear_choice_text')
        if 'link_to_chosen_text' in kwargs:
            self.link_to_chosen_text = kwargs.pop('link_to_chosen_text')
        if 'show_edit_link' in kwargs:
            self.show_edit_link = kwargs.pop('show_edit_link')
        super().__init__(**kwargs)

    class Media:
        js = [
            'generic_chooser/js/chooser-modal.js',
            'generic_chooser/js/chooser-widget.js',
        ]


class SvgChooserAdapter(WidgetAdapter):
    js_constructor = 'wagtail.svg.widgets.SvgChooser'

    def js_args(self, widget):
        return [
            widget.render_html('__NAME__', None, attrs={'id': '__ID__'}),
            widget.id_for_label('__ID__'),
        ]

    class Media:
        js = [
            'generic_chooser/js/chooser-telepath.js',
        ]


register(SvgChooserAdapter(), AdminSvgChooser)
