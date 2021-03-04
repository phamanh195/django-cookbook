from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from myproject.apps.core.models import (
    CreationModificationDateBase,
    MetaTagsBase,
    UrlBase,
    object_relation_base_factory as generic_relation,
)
from myproject.apps.core.model_fields import (
    MultilingualCharField,
    MultilingualTextField,
    TranslateField,
)


class Idea(CreationModificationDateBase, MetaTagsBase, UrlBase):
    title = MultilingualCharField(
        _('Title'),
        max_length=200,
    )
    content = MultilingualTextField(
        _('Content'),
    )

    class Meta:
        verbose_name = _('Idea')
        verbose_name_plural = _('Ideas')

    def __str__(self):
        return self.title

    def get_url_path(self):
        return reverse('idea_details', kwargs={
            'idea_id': str(self.pk)
        })


FavoriteObjectBase = generic_relation(is_required=True)
OwnerBase = generic_relation(
    prefix='owner',
    prefix_verbose=_('Owner'),
    is_required=True,
    add_related_name=True,
    limit_content_type_choices_to={
        'model__in': (
            'user',
            'group',
        )
    }
)


class Idea2(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=200,
    )
    content = models.TextField(
        _('Content'),
    )
    translated_title = TranslateField('title')
    translated_content = TranslateField('content')

    class Meta:
        verbose_name = _('Idea2')
        verbose_name_plural = _('Ideas2')

    def __str__(self):
        return self.title


class Idea2Translations(models.Model):
    idea = models.ForeignKey(
        Idea2,
        verbose_name=_('Idea2'),
        on_delete=models.CASCADE,
        related_name='translations'
    )
    language = models.CharField(_('Language'), max_length=7)

    title = models.CharField(
        _('Title'),
        max_length=200,
    )
    content = models.TextField(
        _('Content')
    )

    class Meta:
        verbose_name = _('Idea2 Translations')
        verbose_name_plural = _('Idea2 Translations')
        ordering = ['idea', 'language']
        unique_together = [['idea', 'language']]

    def __str__(self):
        return self.title


class Like(FavoriteObjectBase, OwnerBase):
    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')

    def __str__(self):
        return _('{owner} likes {object}').format(
            owner=self.owner_content_object,
            object=self.content_object
        )
