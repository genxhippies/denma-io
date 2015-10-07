from django.contrib import admin
from django.forms import SelectMultiple
from django.db import models

from models import Episode, Character

class EpisodeAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'subtitle',
        'publish_date',
        'getCharacters',
    )

    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'10'}) },
    }

admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Character)
