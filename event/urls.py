from django.conf.urls import *
from django.conf import settings
from event import views as event_views

urlpatterns = [
    url(r'^$',event_views.index,name='index'),
	url(r'^user_list$',event_views.user_list,name='user_list'),
	url(r'^user_form$',event_views.user_form,name='user_form'),
	url(r'^users$', event_views.users, name='users'),
	url(r'^users_update/(?P<id>[\d]+)$',event_views.users_update,name='users_update'),
	url(r'^users_remove/(?P<id>[\d]+)$',event_views.users_remove,name='users_remove'),
	
	url(r'^groups$', event_views.groups, name='groups'),
	url(r'^groups_update/(?P<id>[\d]+)$',event_views.groups_update,name='groups_update'),
	url(r'^groups_remove/(?P<id>[\d]+)$',event_views.groups_remove,name='groups_remove'),
]