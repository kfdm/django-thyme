from rest_framework import permissions, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from thyme import models, serializers


class SnapshotViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    queryset = models.Snapshot.objects.all()
    serializer_class = serializers.SnapshotSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            agent=self.request._request.META.get('HTTP_USER_AGENT', 'Unknown'),
        )
