from django.db import models
from django.utils.translation import gettext_lazy as _

from myproject.apps.core.model_fields import (
    MultilingualCharField,
    TranslateField,
)


class Category(models.Model):
    title = models.CharField(_('Title'), max_length=200)

    translated_title = TranslateField('title')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category Translations')
        ordering = ['language']
        unique_together = [['category', 'language']]

    def __str__(self):
        return self.title
