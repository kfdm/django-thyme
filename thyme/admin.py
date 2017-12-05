from django.contrib import admin

from thyme import models


@admin.register(models.Snapshot)
class SnapshotAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'slug', 'owner', 'score', 'active')
    list_filter = ('owner', 'score', 'active')
