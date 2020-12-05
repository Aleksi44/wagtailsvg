import requests
from io import BytesIO
from django.core.files.images import ImageFile
from wagtail.core.blocks import RichTextBlock

from wagtailsvg.models import Svg
from wagtailsvg.blocks import SvgChooserBlock
from tests import constants


# ===============================
# Blocks used for testing purpose
# ===============================


class TextBlock(RichTextBlock):
    def __init__(self, **kwargs):
        super().__init__(features=constants.RICH_TEXT_FEATURES, **kwargs)

    @staticmethod
    def mock(content):
        """
        Mock a TextBlock

        :param content: Format HTML
        :return: Stream content
        """
        return {
            'type': 'text',
            'value': str.strip(content)
        }


class SvgBlock(SvgChooserBlock):
    @staticmethod
    def mock(title):
        """
        Mock a SvgBlock

        :param title: String
        :return: Stream content
        """

        url = str.strip(constants.SVG_1_URL)
        filename = "%s.svg" % title
        try:
            ret = Svg.objects.get(title=title)
        except Svg.DoesNotExist:
            response = requests.get(url)
            file = ImageFile(BytesIO(response.content), name=filename)
            ret = Svg(
                title=title,
                file=file
            )
            ret.save()
        return {
            'type': 'svg',
            'value': ret.id
        }
