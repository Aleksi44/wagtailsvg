import os
from io import BytesIO

from django.core.files.storage import default_storage
from django.core.files.images import ImageFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from wagtail.core.models import CollectionMember
from wagtail.admin.edit_handlers import TabbedInterface
from wagtail.search import index
from wagtail.admin.edit_handlers import ObjectList
from wagtail.admin.edit_handlers import FieldPanel

from taggit.managers import TaggableManager


class Svg(CollectionMember, index.Indexed, models.Model):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    file = models.FileField(
        upload_to=getattr(settings, 'WAGTAILSVG_UPLOAD_FOLDER', 'media'),
        verbose_name=_("file")
    )
    tags = TaggableManager(help_text=None, blank=True, verbose_name=_("tags"))
    edit_code = models.TextField(default='', blank=True)

    class Meta:
        ordering = ['-id']

    admin_form_fields = (
        "title",
        "file",
        "collection",
        "tags",
    )

    edit_handler = TabbedInterface([
        ObjectList([
            FieldPanel('collection'),
            FieldPanel('title'),
            FieldPanel('file'),
            FieldPanel('tags'),
        ], heading="General"),
        # EditCodePanel()
    ])

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    @property
    def file_content(self):
        if self.file:
            # TODO: condition if external url
            f = default_storage.open(self.file.name, 'r')
            return f.read()
        return ''

    @property
    def url(self):
        return self.file.url

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        instance._state.adding = False
        instance._state.db = db
        instance._old_values = dict(zip(field_names, values))
        return instance

    def save(self, *args, **kwargs):
        if self.edit_code and not self.data_changed(['file']):
            # Update file with edit_code

            self.file = ImageFile(
                BytesIO(self.edit_code.encode()),
                name=self.filename
            )

        # Keep empty `edit_code` to not save SVG content in database
        self.edit_code = ''
        super(Svg, self).save(*args, **kwargs)

    def data_changed(self, fields):
        """
        example:
        if self.data_changed(['street', 'city', 'country']):
            print("one of the fields changed")
        returns true if the model saved the first time
        and _old_values doesnt exist
        :param fields:
        :return:
        """
        if hasattr(self, '_old_values'):
            if not self.pk or not self._old_values:
                return True

            for field in fields:
                if getattr(self, field) != self._old_values[field]:
                    return True
            return False

        return True
