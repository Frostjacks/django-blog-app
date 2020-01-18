from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# this creates the profile every time a user a created
@receiver(post_save, sender=User)  # this means: when a user is saved send this signal and that is received by this receiver named create_profile
def create_profile(sender, instance, created, **kwargs):    # kwargs means accept any other additional keyword arguments
    # instance is the instance of a user
    if created: # if user is created
        Profile.objects.create(user=instance)  # then create this profile object with that instant of user. Profile is a model name so is capital


# this actually saves the profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()   # this profile is a field of user table so is in lower case