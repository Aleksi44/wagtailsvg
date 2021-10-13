from django.utils.functional import cached_property
from django.utils.html import format_html
from wagtail.core.blocks import ChooserBlock


class SvgChooserBlock(ChooserBlock):
    @cached_property
    def target_model(self):
        from wagtailsvg.models import Svg
        return Svg

    @cached_property
    def widget(self):
        from wagtailsvg.widgets import AdminSvgChooser
        return AdminSvgChooser()

    def render_basic(self, value, context=None):
        if value:
            return format_html(
                "<img src='{0}' alt='{1}'>",
                value.url,
                value.title
            )
        else:
            return ''

    def get_form_state(self, value):
        value_data = self.widget.get_value_data(value)
        if value_data is None:
            return None
        else:
            return {
                'id': value_data['id'],
                'edit_link': value_data['edit_url'],
                'title': value_data['title'],
                'preview_url': value_data['preview_url'],
            }
