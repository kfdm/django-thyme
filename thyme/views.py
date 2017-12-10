
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView

from thyme import models


class SnapshotList(LoginRequiredMixin, ListView):
    model = models.Snapshot
    paginate_by = 50

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user, active=True)


class BlacklistList(LoginRequiredMixin, ListView):
    model = models.Blacklist
    paginate_by = 50

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)

    def post(self, request):
        if 'create' in request.POST:
            obj, created = models.Blacklist.objects.get_or_create(
                slug=request.POST['create'],
                owner=request.user
            )
            if created:
                messages.add_message(
                    request,
                    messages.INFO,
                    _('Blacklisted %s') % obj.slug
                )
        if 'delete' in request.POST:
            result = models.Blacklist.objects.filter(
                slug=request.POST['delete'],
                owner=request.user
            ).delete()
            messages.add_message(
                request,
                messages.INFO,
                _('Removed %s from blacklist') % request.POST['delete']
                )
        return self.get(request)
