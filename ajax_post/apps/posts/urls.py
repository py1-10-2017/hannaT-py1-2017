from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^post_json$', views.post_json),
    url(r'^json_posts$', views.json_posts)      
]
