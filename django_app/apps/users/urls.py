from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new$', views.new),
    url(r'^/register$', views.new),
    url(r'^login$', views.create),
    url(r'^$', views.index)

    
]

