from django.contrib import admin
from app_profile.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'profile'
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)