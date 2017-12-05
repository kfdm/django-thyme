import os

from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

from thyme.models import Snapshot

DIR_NAME = os.path.dirname(__file__)


class TestImport(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(id=999, username="Foo")

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def test_macos(self):
        self.client.force_login(self.user)
        with open(os.path.join(DIR_NAME, 'test.macos.json')) as fp:
            response = self.client.post(
                path=reverse('api:snapshot-macos'),
                data=fp.read(),
                content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Snapshot.objects.count(), 2, 'Should result in 2 Snapshots')

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def est_cli(self):
        self.client.force_login(self.user)
        with open(os.path.join(DIR_NAME, 'test.cli.json')) as fp:
            response = self.client.post(
                path=reverse('api:snapshot-bulk-import'),
                data=fp.read(),
                content_type='application/json'
            )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Snapshot.objects.count(), 2, 'Should result in 2 Snapshots')

    @override_settings(CELERY_TASK_ALWAYS_EAGER=True)
    def est_chrome(self):
        self.client.force_login(self.user)
        with open(os.path.join(DIR_NAME, 'test.chrome.json')) as fp:
            response = self.client.post(
                path=reverse('api:snapshot-list'),
                data=fp.read(),
                content_type='application/json'
            )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Snapshot.objects.count(), 3, 'Should result in 3 Snapshots')
