from rest_framework import serializers
from thyme import models


class SnapshotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Snapshot
        fields = ('timestamp', 'owner', 'agent', 'score', 'active')
        read_only = ('agent',)


class BlacklistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.Blacklist
        fields = ('slug', 'owner')
