from proyectalo.models import User, Ideologist, Builder
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def makeJob(sender, instance, created, **kwargs):
    if created:
        if instance.job_type == 1:
            Ideologist.objects.create(user=instance)
        if instance.job_type == 2:
            Builder.objects.create(user=instance)