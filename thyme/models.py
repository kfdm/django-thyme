from django.db import models
from django.utils.translation import ugettext_lazy as _


class Snapshot(models.Model):
    owner = models.ForeignKey('auth.User', related_name='quotes', verbose_name=_('owner'))
    timestamp = models.DateTimeField()
    data = models.TextField()
