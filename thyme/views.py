
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from thyme import models


class SnapshotList(LoginRequiredMixin, ListView):
    model = models.Snapshot
    paginate_by = 50

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user, active=True)
