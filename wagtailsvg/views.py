from wagtailsvg.models import Svg
from generic_chooser.views import \
    ModelChooserViewSet, \
    ChooserListingTabMixin, \
    ModelChooserMixin


class SvgChooserListingTab(ChooserListingTabMixin):
    def get_row_data(self, item):
        return {
            'choose_url': self.get_chosen_url(item),
            'title': item.title,
            'url': item.url,
        }


class SvgModelChooserMixin(ModelChooserMixin):
    def get_chosen_response_data(self, item):
        """
        Generate the result value to be returned when an object has been chosen
        """
        response_data = super().get_chosen_response_data(item)
        response_data['preview_url'] = item.file.url
        return response_data


class SvgChooserViewSet(ModelChooserViewSet):
    model = Svg
    icon = 'image'
    page_title = "Choose a Svg"
    listing_tab_mixin_class = SvgChooserListingTab
    chooser_mixin_class = SvgModelChooserMixin
    edit_item_url_name = 'wagtailsvg_svg_modeladmin_edit'
