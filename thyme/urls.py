from django.conf.urls import url

from thyme import views

urlpatterns = [
    url(r'snapshot$', views.SnapshotList.as_view(), name='snapshot-list'),
    url(r'blacklist$', views.BlacklistList.as_view(), name='blacklist-list'),
]
