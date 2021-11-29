from wagtail.admin.edit_handlers import BaseChooserPanel


class SvgChooserPanel(BaseChooserPanel):
    object_type_name = "svg"

    def widget_overrides(self):
        from wagtailsvg.widgets import AdminSvgChooser
        return {self.field_name: AdminSvgChooser}
