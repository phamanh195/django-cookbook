from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):


    def get_ideas_without_this_category(self):
        from myproject.apps.ideas.models import Idea
        return Idea.objects.exclude(category=self)
