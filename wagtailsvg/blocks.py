from django.utils.functional import cached_property
from wagtail.core.blocks import ChooserBlock


class SvgChooserBlock(ChooserBlock):
    @cached_property
    def target_model(self):
        from wagtailsvg.models import Svg
        return Svg

    @cached_property
    def widget(self):
        from wagtailsvg.widgets import AdminSvgChooser
        return AdminSvgChooser

    def render_basic(self, value, context=None):
        return "<img src='%s' alt='%s'>" % (
            value.url,
            value.title
        )
