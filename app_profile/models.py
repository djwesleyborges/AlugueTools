from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(_('Address'), max_length=200, blank=True)
    city = models.CharField(_('City'), max_length=40, blank=True, null=True)
    birth_date = models.DateField(_('Birth Date'), null=True, blank=True)
    photo = models.ImageField(verbose_name=_('Profile Picture'), upload_to='profile_image/', max_length=255, null=True)
    phone = models.CharField(max_length=20, blank=True, default='')

    # Importante: Devemos criar métodos de @receiver para que o Django crie um perfil automaticamente ao criar um
    # usuário.
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #     instance.profile.save()

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = Profile(user=user)
            user_profile.save()
    post_save.connect(create_profile, sender=User)