try:
    from wagtail.admin.panels import FieldPanel
    from wagtailsvg.widgets import AdminSvgChooser

    class SvgChooserPanel(FieldPanel):
        def __init__(self, field_name, disable_comments=None, permission=None, **kwargs):
            super().__init__(field_name, **kwargs)
            self.widget = AdminSvgChooser
            self.disable_comments = disable_comments
            self.permission = permission

except ImportError:
    from wagtail.admin.edit_handlers import BaseChooserPanel

    class SvgChooserPanel(BaseChooserPanel):
        object_type_name = "svg"

        def widget_overrides(self):
            from wagtailsvg.widgets import AdminSvgChooser
            return {self.field_name: AdminSvgChooser}
