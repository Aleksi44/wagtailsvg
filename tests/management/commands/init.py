import json
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from wagtail.core.models import Page, Site
from wagtailsvg.models import Svg

from tests.models import TestPage
from tests.blocks import TextBlock, SvgBlock
from tests import constants


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        Reset and initialize test data
        """
        Site.objects.all().delete()
        Page.objects.all().delete()
        Svg.objects.all().delete()

        text = TextBlock()
        svg = SvgBlock()

        # Create admin user

        user, created = User.objects.get_or_create(
            username='wagtail',
            first_name='User',
            last_name='Admin',
            email='test@test.test',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        if created:
            user.save()
            user.set_password('svg')
            for group in Group.objects.all():
                user.groups.add(group)
            user.save()

        #  Create RootPage, HomePage, Site

        page_content_type, created = ContentType.objects.get_or_create(
            model='page',
            app_label='wagtailcore'
        )

        root = Page.objects.create(
            title="Root",
            slug='root',
            content_type=page_content_type,
            path='0001',
            depth=1,
            numchild=1,
            url_path='/',
        )
        root.save()

        home_page = TestPage.objects.create(
            title="Examples - Test page",
            slug='home',
            path='00010001',
            depth=2,
            numchild=0,
            body=json.dumps([
                text.mock(constants.WELCOME_TEXT),
            ])
        )
        home_page.save()

        site = Site.objects.create(
            hostname='localhost',
            port=8080,
            root_page_id=home_page.id,
            is_default_site=True
        )
        site.save()

        # Page Examples -------------------------------------------------------

        content_page = TestPage(
            title="Example 1",
            seo_title="Example 1",
            search_description="Example 1",
            slug='example-1',
            logo_id=svg.mock('logo')['value'],
            body=json.dumps([
                text.mock(constants.TEXT_1),
                svg.mock('svg-example-1'),
                text.mock(constants.TEXT_1),
            ])
        )
        home_page.add_child(instance=content_page)

        content_page = TestPage(
            title="Example 2",
            seo_title="Example 2",
            search_description="Example 2",
            slug='example-2',
            logo_id=svg.mock('logo')['value'],
            body=json.dumps([
                text.mock(constants.TEXT_1),
                svg.mock('svg-example-2'),
                text.mock(constants.TEXT_1),
            ])
        )
        home_page.add_child(instance=content_page)
