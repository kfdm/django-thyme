import json

from dateutil.parser import parse
from rest_framework import permissions, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.decorators import list_route
from rest_framework.response import Response
from thyme import models, serializers


class SnapshotViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    queryset = models.Snapshot.objects.all()
    serializer_class = serializers.SnapshotSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user,
            agent=self.request._request.META.get('HTTP_USER_AGENT', 'Unknown'),
        )

    @list_route(methods=['post'])
    def macos(self, request):
        count = 0
        body = json.loads(request.body.decode("utf-8"))
        ts = parse(body['timeCollected']).replace(second=0, microsecond=0)
        for app in body.get('runningProcesses', []):
            models.Snapshot.objects.create(
                owner=request.user,
                timestamp=ts,
                slug=app['appBundle'],
                score=0,
                active=app['isActive'],
                agent=request.META.get('HTTP_USER_AGENT', 'Unknown'),
                raw=json.dumps(app)
            )
            count += 1
        return Response({'created': count})
