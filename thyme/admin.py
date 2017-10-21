from django.contrib import admin

from thyme import models


@admin.register(models.Snapshot)
class SnapshotAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'owner')
    list_filter = ('owner',)
