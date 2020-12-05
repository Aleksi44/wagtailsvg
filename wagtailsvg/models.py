import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.core.models import CollectionMember
from wagtail.search import index
from taggit.managers import TaggableManager


class Svg(CollectionMember, index.Indexed, models.Model):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    file = models.FileField(upload_to="media", verbose_name=_("file"))
    tags = TaggableManager(help_text=None, blank=True, verbose_name=_("tags"))

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    @property
    def url(self):
        return self.file.url

    admin_form_fields = (
        "title",
        "file",
        "collection",
        "tags",
    )

    def __str__(self):
        return self.title
