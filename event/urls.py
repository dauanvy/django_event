from django.conf.urls import *
from django.conf import settings
from event import views as event_views
from django.views.generic import ListView, DetailView

from event.models import Event
urlpatterns = [
    url(r'^$',event_views.index,name='index'),
	url(r'^detail/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(model=Event),name='event'),
	#url(r'^posts/(?P<id>\d+)/(?P<slug>[\w-]+)$', DetailView.as_view(model=Event), name='post'),
	
	url(r'^users$', event_views.users, name='users'),
	url(r'^users_update/(?P<id>[\d]+)$',event_views.users_update,name='users_update'),
	url(r'^users_remove/(?P<id>[\d]+)$',event_views.users_remove,name='users_remove'),
	
	url(r'^groups$', event_views.groups, name='groups'),
	url(r'^groups_update/(?P<id>[\d]+)$',event_views.groups_update,name='groups_update'),
	url(r'^groups_remove/(?P<id>[\d]+)$',event_views.groups_remove,name='groups_remove'),
	
	url(r'^event$', event_views.event, name='event'),
	url(r'^event_update/(?P<id>[\d]+)$',event_views.event_update,name='event_update'),
	url(r'^event_remove/(?P<id>[\d]+)$',event_views.event_remove,name='event_remove'),
	
	url(r'^location$',event_views.location,name='location'),
	url(r'^location_update/(?P<id>[\d]+)$',event_views.location_update,name='location_update'),
	url(r'^location_remove/(?P<id>[\d]+)$',event_views.location_remove,name='location_remove'),
	
	url(r'^category$',event_views.category,name='category'),
	url(r'^category_update/(?P<id>[\d]+)$',event_views.category_update,name='category_update'),
	url(r'^category_remove/(?P<id>[\d]+)$',event_views.category_remove,name='category_remove'),
	
	url(r'^web/login$',event_views.event_login,name='event_login'),
	url(r'^web/signup$',event_views.event_signup,name='event_signup'),
	url(r'^web/logout$',event_views.event_logout,name='event_logout'),
	url(r'^web/success$',event_views.event_success,name='event_success'),	
]