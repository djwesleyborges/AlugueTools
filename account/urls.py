from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from account.views import RegisterUserView, DashboardView
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^dashboard/$', view=DashboardView.as_view(), name='dashboard')
]