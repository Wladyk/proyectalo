from proyectalo.models import User, Seeker, Offerer
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def makeJob(sender, instance, created, **kwargs):
    if created:
        if instance.seekerFlag == True:
            Seeker.objects.create(user=instance)
        if instance.offererFlag == True:
            Offerer.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()