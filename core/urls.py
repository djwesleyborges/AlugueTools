from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^$', views.contact, name='contact'),
]

'''
\w - Qualquer caracter alfanumerico,(qualquer letra ou numero).
_- - Pode conter _ ou - na url

'''