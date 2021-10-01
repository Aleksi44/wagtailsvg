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

    def get_object_list(self, search_term=None, **kwargs):
        if search_term:

            # TODO: Fix search backend (it does not filter correctly)
            # search_backend = get_search_backend()
            # object_list = search_backend.search(search_term, object_list)

            return Svg.objects.filter(title__icontains=search_term)
        return self.get_unfiltered_object_list()


class SvgChooserViewSet(ModelChooserViewSet):
    model = Svg
    icon = 'image'
    page_title = "Choose a Svg"
    listing_tab_mixin_class = SvgChooserListingTab
    chooser_mixin_class = SvgModelChooserMixin
    edit_item_url_name = 'wagtailsvg_svg_modeladmin_edit'
    per_page = 10
