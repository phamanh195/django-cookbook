from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from myproject.apps.core.admin import (
    get_multilingual_field_names,
    LanguageChoicesForm
)
from .models import Idea, Idea2, Idea2Translations


class Idea2TranslationForm(LanguageChoicesForm):
    class Meta:
        model = Idea2Translations
        fields = '__all__'


class Idea2TranslationInline(admin.StackedInline):
    form = Idea2TranslationForm
    model = Idea2Translations
    extra = 0


@admin.register(Idea2)
class Idea2Admin(admin.ModelAdmin):
    inlines = [Idea2TranslationInline]
    fieldsets = [
        (_('Title and Content'), {
            'fields': ['title', 'content']
        })
    ]


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Title and Content'), {
            'fields': get_multilingual_field_names('title') + get_multilingual_field_names('content')
        })
    ]
