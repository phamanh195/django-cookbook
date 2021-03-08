import uuid

from django.db import models
from django.urls import reverse
from django.conf import settings
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


RATING_CHOICES = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★"),
)


class Idea(CreationModificationDateBase, UrlBase):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4(), editable=False
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Author'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='authored_ideas',
    )
    title = models.CharField(_('Title'), max_length=200)
    content = models.TextField(_('Content'))

    categories = models.ManyToManyField(
        'categories.Category',
        verbose_name=_('Categories'),
        related_name='category_ideas',
    )
    rating = models.PositiveIntegerField(
        _('Rating'), choices=RATING_CHOICES, blank=True, null=True
    )
    translated_title = TranslateField('title')
    translated_content = TranslateField('content')

    class Meta:
        verbose_name = _('Idea')
        verbose_name_plural = _('Ideas')

    def __str__(self):
        return self.title

    def get_url_path(self):
        return reverse('ideas:ideal_detail', kwargs={'pk': self.pk})


class IdeaTranslations(models.Model):
    idea = models.ForeignKey(
        Idea,
        verbose_name=_('Idea'),
        on_delete=models.CASCADE,
        related_name='translation',
    )
    language = models.CharField(_('Language'), max_length=7)

    title = models.CharField(_('Title'), max_length=200)
    content = models.TextField(_('Content'))

    class Meta:
        verbose_name = _('Idea Translations')
        verbose_name_plural = _('Idea Translations')
        ordering = ['language']
        unique_together = [['idea', 'language']]

    def __str__(self):
        return self.title





#
#
# class Idea(CreationModificationDateBase, MetaTagsBase, UrlBase):
#     title = MultilingualCharField(
#         _('Title'),
#         max_length=200,
#     )
#     content = MultilingualTextField(
#         _('Content'),
#     )
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         verbose_name=_('Author'),
#         on_delete=models.SET_NULL,
#         blank=True,
#         null=True,
#     )
#     category = models.ForeignKey(
#         'categories.Category',
#         verbose_name=_('Category'),
#         blank=True,
#         null=True,
#         on_delete=models.SET_NULL,
#     )
#
#     class Meta:
#         verbose_name = _('Idea')
#         verbose_name_plural = _('Ideas')
#
#     def __str__(self):
#         return self.title
#
#     def get_url_path(self):
#         return reverse('idea_details', kwargs={
#             'idea_id': str(self.pk)
#         })
#
#
# FavoriteObjectBase = generic_relation(is_required=True)
# OwnerBase = generic_relation(
#     prefix='owner',
#     prefix_verbose=_('Owner'),
#     is_required=True,
#     add_related_name=True,
#     limit_content_type_choices_to={
#         'model__in': (
#             'user',
#             'group',
#         )
#     }
# )
#
#
# class Idea2(models.Model):
#     title = models.CharField(
#         _('Title'),
#         max_length=200,
#     )
#     content = models.TextField(
#         _('Content'),
#     )
#     translated_title = TranslateField('title')
#     translated_content = TranslateField('content')
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         verbose_name=_('Author'),
#         on_delete=models.SET_NULL,
#         blank=True,
#         null=True,
#     )
#     categories = models.ManyToManyField(
#         'categories.Category',
#         verbose_name=_('Categories'),
#         blank=True,
#         related_name='ideas2'
#     )
#
#     class Meta:
#         verbose_name = _('Idea2')
#         verbose_name_plural = _('Ideas2')
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['title'],
#                 condition=~models.Q(author=None),
#                 name='unique_title_for_each_author'
#             ),
#             models.CheckConstraint(
#                 check=models.Q(
#                     title__iregex=r'^\S.*\S$'
#                 ),
#                 name='title_has_no_leading_and_trailing_whitespaces',
#             )
#         ]
#
#     def __str__(self):
#         return self.title
#
#
# class Idea2Translations(models.Model):
#     idea = models.ForeignKey(
#         Idea2,
#         verbose_name=_('Idea2'),
#         on_delete=models.CASCADE,
#         related_name='translations'
#     )
#     language = models.CharField(_('Language'), max_length=7)
#
#     title = models.CharField(
#         _('Title'),
#         max_length=200,
#     )
#     content = models.TextField(
#         _('Content')
#     )
#
#     class Meta:
#         verbose_name = _('Idea2 Translations')
#         verbose_name_plural = _('Idea2 Translations')
#         ordering = ['idea', 'language']
#         unique_together = [['idea', 'language']]
#
#     def __str__(self):
#         return self.title
#
#
# class Like(FavoriteObjectBase, OwnerBase):
#     class Meta:
#         verbose_name = _('Like')
#         verbose_name_plural = _('Likes')
#
#     def __str__(self):
#         return _('{owner} likes {object}').format(
#             owner=self.owner_content_object,
#             object=self.content_object
#         )
