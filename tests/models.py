from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtailsvg.edit_handlers import SvgChooserPanel
from wagtailsvg.models import Svg
from .blocks import TextBlock, SvgBlock


# =================================
# TestPage used for testing purpose
# =================================


class TestPage(Page):
    logo = models.ForeignKey(
        Svg, related_name='+',
        null=True, blank=True, on_delete=models.SET_NULL
    )
    body = StreamField([
        ('text', TextBlock()),
        ('svg', SvgBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        SvgChooserPanel('logo'),
        StreamFieldPanel('body'),
    ]
