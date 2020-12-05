from wagtail.admin.edit_handlers import BaseChooserPanel
from wagtailsvg.widgets import AdminSvgChooser


class SvgChooserPanel(BaseChooserPanel):
    object_type_name = "svg"

    def widget_overrides(self):
        return {self.field_name: AdminSvgChooser}
