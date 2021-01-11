from django.utils.translation import gettext_lazy as _
from generic_chooser.widgets import AdminChooser
from wagtailsvg.models import Svg


class AdminSvgChooser(AdminChooser):
    choose_one_text = _("Choose a SVG item")
    choose_another_text = _("Choose another SVG item")
    link_to_chosen_text = _("Edit this SVG item")
    model = Svg
    choose_modal_url_name = 'svg_chooser:choose'
    edit_item_url_name = 'wagtailsvg_svg_modeladmin_edit'
