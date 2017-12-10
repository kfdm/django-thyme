from django.db import models
from django.utils.translation import ugettext_lazy as _


class Snapshot(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    slug = models.CharField(max_length=128)
    active = models.BooleanField(default=False)
    score = models.IntegerField()
    agent = models.CharField(max_length=128)

    raw = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']


class Blacklist(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    slug = models.CharField(max_length=128)

    class Meta:
        ordering = ['slug']
        unique_together = (("owner", "slug"),)
