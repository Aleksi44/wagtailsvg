from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from wagtail.core import hooks
from wagtailsvg.views import SvgChooserViewSet
from wagtailsvg.models import Svg


@hooks.register('register_admin_viewset')
def register_site_chooser_viewset():
    return SvgChooserViewSet('svg_chooser', url_prefix='svg-chooser')


class SvgModelAdmin(ModelAdmin):
    model = Svg
    menu_label = 'Svg'
    menu_icon = 'image'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


modeladmin_register(SvgModelAdmin)
