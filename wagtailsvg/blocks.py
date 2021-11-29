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

    def get_form_state(self, value):
        return self.widget.get_value_data(value)

    def render_basic(self, value, context=None):
        if value:
            return format_html(
                "<img src='{0}' alt='{1}'>",
                value.url,
                value.title
            )
        else:
            return ''
