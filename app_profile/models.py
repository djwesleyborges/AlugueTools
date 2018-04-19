from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import choice
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(_('Address'), max_length=200, blank=True)
    city = models.CharField(_('City'), max_length=40, blank=True, null=True)
    birth_date = models.DateField(_('Birth Date'), null=True, blank=True)
    token = models.CharField(_('Token'), max_length=15, unique=True, db_index=True, null=True)

    def set_token(self):
        self.token = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(15)])

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        self.set_token()
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()