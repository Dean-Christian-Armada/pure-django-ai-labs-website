from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='blogs_index' ),
	url(r'^(?P<slug>[\w\-]+)/$', views.item, name='blogs_item' ),
]