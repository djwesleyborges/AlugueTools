from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from account.views import RegisterUserView, HomeView
from django.contrib.auth.views import login
from app_profile.views import panel_user, edit_account, edit_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^home/$', view=HomeView.as_view(), name='home'),
    url(r'^panel/$', panel_user, name='panel_user'),
    url(r'^edit_account/$', edit_account, name='edit_account'),
    url(r'^edit_password/$', edit_password, name='edit_password'),
    url(r'^password_reset/$', view=auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view=auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]