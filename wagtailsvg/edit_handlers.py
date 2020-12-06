from wagtail.admin.edit_handlers import BaseChooserPanel
from wagtail.admin.edit_handlers import ObjectList
from wagtail.admin.edit_handlers import FieldPanel


class EditCodeField(FieldPanel):
    object_template = "wagtailsvg/edit_handlers/edit_code_object.html"


class EditCodePanel(ObjectList):
    template = "wagtailsvg/edit_handlers/edit_code_panel.html"

    def __init__(self, *args, **kwargs):
        children = [
            EditCodeField('edit_code'),
        ]
        super().__init__(children=children, heading='Edit Code')


class SvgChooserPanel(BaseChooserPanel):
    object_type_name = "svg"

    def widget_overrides(self):
        from wagtailsvg.widgets import AdminSvgChooser
        return {self.field_name: AdminSvgChooser}
