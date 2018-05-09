from django.conf.urls import url
from django.contrib.auth import views as auth_views
from app_profile.views import panel_user, edit_account, edit_password
from account.views import RegisterUserView, HomeView, do_login, do_logout

urlpatterns = [
    url(r'^$', do_login, name='login'),
    url(r'^logout/$', do_logout, name='logout'),
    url(r'^panel/$', panel_user, name='panel_user'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^edit_account/$', edit_account, name='edit_account'),
    url(r'^edit_password/$', edit_password, name='edit_password'),
    url(r'^register/$', RegisterUserView.as_view(), name='register'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view=auth_views.password_reset_confirm, name='password_reset_confirm'),
]
