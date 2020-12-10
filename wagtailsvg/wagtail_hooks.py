# import json
# from django.utils.html import format_html, format_html_join, mark_safe
# from django.templatetags.static import static
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from wagtail.core import hooks
from wagtailsvg.views import SvgChooserViewSet
from wagtailsvg.models import Svg


# from wagtailsvg import context


@hooks.register('register_admin_viewset')
def register_site_chooser_viewset():
    return SvgChooserViewSet('svg_chooser', url_prefix='svg-chooser')


"""
@hooks.register('insert_editor_js')
def edit_code_panel_js():
    cxt = json.dumps({
        'version': context.VERSION,
    })
    js_files = [
        'wagtailsvg/dist/js/app%s.js' % context.VERSION,
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files)
    )
    js_exec = format_html(
        "<script>{}</script>",
        mark_safe(
            "$(function() {"
            "const panel = new WagtailSvg.EditCodePanel(%s);"
            "panel.init();"
            "});" % cxt)
    )
    return js_includes + js_exec
"""


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
