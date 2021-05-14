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
        return AdminSvgChooser()

    def render_basic(self, value, context=None):
        return "<img src='%s' alt='%s'>" % (
            value.url,
            value.title
        )

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
