from wagtailsvg.models import Svg
from wagtail import VERSION as WAGTAIL_VERSION
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from generic_chooser.widgets import AdminChooser
from django.core.exceptions import ObjectDoesNotExist


class AdminSvgChooser(AdminChooser):
    choose_one_text = _("Choose an SVG")
    choose_another_text = _("Choose another SVG")
    link_to_chosen_text = _("Edit this SVG")
    model = Svg
    choose_modal_url_name = 'svg_chooser:choose'
    edit_item_url_name = 'wagtailsvg_svg_modeladmin_edit'
    clear_choice_text = _("Clear choice")
    template = 'wagtailsvg/widgets/chooser.html'

    def get_value_data(self, value):
        if value is None:
            instance = None
        elif self.model and isinstance(value, self.model):
            instance = value
            value = value.pk
        else:
            try:
                instance = self.get_instance(value)
            except (ObjectDoesNotExist if self.model is None else self.model.DoesNotExist):
                instance = None
        if instance is None:
            return {
                'value': None,
                'title': '',
                'edit_item_url': None,
                'preview_url': None,
            }
        else:
            return {
                'value': value,
                'title': self.get_title(instance),
                'edit_item_url': self.get_edit_item_url(instance),
                'preview_url': instance.url,
            }

    def render_html(self, name, value, attrs):
        if WAGTAIL_VERSION >= (2, 12):
            value_data = value
        else:
            value_data = self.get_value_data(value)

        original_field_html = self.render_input_html(name, value_data['value'], attrs)
        return render_to_string(self.template, {
            'widget': self,
            'original_field_html': original_field_html,
            'attrs': attrs,
            'is_empty': value_data['value'] is None,
            'title': value_data['title'],
            'edit_item_url': value_data['edit_item_url'],
            'create_item_url': self.get_create_item_url(),
            'choose_modal_url': self.get_choose_modal_url(),
            'preview_url': value_data['preview_url']
        })

    class Media:
        js = [
            'generic_chooser/js/chooser-modal.js',
            'wagtailsvg/js/chooser-widget.js',
        ]
