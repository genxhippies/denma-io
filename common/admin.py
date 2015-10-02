from django.contrib import admin

from models import Episode

class EpisodeAdmin(admin.ModelAdmin):
    list_display = (
        'num',
        'subtitle',
        'publish_date',
    )

admin.site.register(Episode, EpisodeAdmin)
