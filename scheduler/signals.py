from .models import Profile
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(
      user=instance,
      username=instance.username)


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
  if created == False:
    profile = instance.profile
    profile.email = instance.email
    profile.first_name = instance.first_name
    profile.last_name = instance.last_name
    profile.save()


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
  instance.user.delete()
