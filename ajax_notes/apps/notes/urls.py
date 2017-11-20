from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^show_notes$', views.show_notes), 
    url(r'^create$', views.create),
    url(r'^edit$', views.edit),
    url(r'^delete$', views.delete)      
]