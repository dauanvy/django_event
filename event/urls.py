from django.conf.urls import *
from django.conf import settings
from event import views as event_views

urlpatterns = [
    url(r'^$',event_views.index,name='index'),

	url(r'^users$', event_views.users, name='users'),
	url(r'^users_update/(?P<id>[\d]+)$',event_views.users_update,name='users_update'),
	url(r'^users_remove/(?P<id>[\d]+)$',event_views.users_remove,name='users_remove'),
	
	url(r'^groups$', event_views.groups, name='groups'),
	url(r'^groups_update/(?P<id>[\d]+)$',event_views.groups_update,name='groups_update'),
	url(r'^groups_remove/(?P<id>[\d]+)$',event_views.groups_remove,name='groups_remove'),
	
	url(r'^event$', event_views.event, name='event'),
	url(r'^event_update/(?P<id>[\d]+)$',event_views.event_update,name='event_update'),
	url(r'^event_remove/(?P<id>[\d]+)$',event_views.event_remove,name='event_remove'),
	
	url(r'^web/login$',event_views.event_login,name='event_login'),
	url(r'^web/signup$',event_views.event_signup,name='event_signup'),
]