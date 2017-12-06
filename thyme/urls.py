from thyme import views

from django.conf.urls import url

urlpatterns = [
    url(r'snapshot$', views.SnapshotList.as_view(), name='snapshot-list'),
]
