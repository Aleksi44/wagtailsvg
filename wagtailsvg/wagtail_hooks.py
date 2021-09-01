from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from wagtail.core import hooks
from wagtail.admin.site_summary import SummaryItem
from wagtailsvg.views import SvgChooserViewSet
from wagtailsvg.models import Svg


class SvgSummaryItem(SummaryItem):
    order = 290
    template = "wagtailsvg/homepage/site_summary_svg.html"

    def get_context(self):
        return {
            "total_svg": Svg.objects.count(),
        }


@hooks.register("construct_homepage_summary_items")
def add_svg_summary_item(request, items):
    items.append(SvgSummaryItem(request))


@hooks.register('register_admin_viewset')
def register_site_chooser_viewset():
    return SvgChooserViewSet('svg_chooser', url_prefix='svg-chooser')


class SvgModelAdmin(ModelAdmin):
    model = Svg
    menu_label = 'Svg'
    menu_icon = 'image'
    menu_order = 400
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title',)
    list_filter = ('collection__name',)
    search_fields = ('title',)


modeladmin_register(SvgModelAdmin)
