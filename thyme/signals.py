from django.db.models.signals import post_save
from django.apps import apps
from django.dispatch import receiver


@receiver(post_save, sender='thyme.Blacklist')
def remove_blacklisted_snapshots(sender, created, instance, **kwargs):
    if created:
        Snapshot = apps.get_model('thyme.Snapshot')
        qs = Snapshot.objects.filter(
            owner=instance.owner,
            slug=instance.slug,
        ).delete()
