from django.conf.urls import *
from django.conf import settings
from event import views as event_views

urlpatterns = [
    url(r'^$',event_views.index,name='index'),
	url(r'^user_list$',event_views.user_list,name='user_list'),
	url(r'^user_form$',event_views.user_form,name='user_form'),
]