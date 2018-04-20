from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from account.views import RegisterUserView, HomeView
from django.contrib.auth.views import login
from app_profile.views import panel_user, edit_account


urlpatterns = [
    url(r'^$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^home/$', view=HomeView.as_view(), name='home'),
    url(r'^panel/$', panel_user, name='panel_user'),
    url(r'^edit_account/$', edit_account, name='edit_account'),
]