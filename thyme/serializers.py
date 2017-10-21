from rest_framework import serializers
from thyme import models
from dateutil.parser import parse


class SnapshotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Snapshot
        fields = ('id', 'timestamp', 'data', 'owner', 'agent')
        read_only = ('id',)

    def to_internal_value(self, data):
        return {
            'data': data,
            'timestamp': parse(data['Time']),
        }
