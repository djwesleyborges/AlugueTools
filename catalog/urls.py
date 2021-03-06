from django.conf.urls import url
from catalog import views


urlpatterns = [
    url(r'^$', views.catalog_list, name='product_list'),
    url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    url(r'^product/(?P<slug>[\w_-]+)/$', views.product, name='product'),
]

'''
\w - Qualquer caracter alfanumerico,(qualquer letra ou numero).
_- - Pode conter _ ou - na url

'''