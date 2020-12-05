from wagtailsvg.models import Svg
from generic_chooser.views import ModelChooserViewSet, ChooserListingTabMixin


class SvgChooserListingTab(ChooserListingTabMixin):
    def get_row_data(self, item):
        return {
            'choose_url': self.get_chosen_url(item),
            'title': item.title,
            'url': item.url,
        }


class SvgChooserViewSet(ModelChooserViewSet):
    model = Svg
    icon = 'image'
    page_title = "Choose a Svg"
    listing_tab_mixin_class = SvgChooserListingTab
