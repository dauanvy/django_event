from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect, Http404
from event.models import EventUsers, EventUsersForm
from event.models import EventGroups, EventGroupsForm
from event.models import Event, EventForm

def index(request):
	data = {}
	list_item = Event.objects.all()
	data['list_item'] = list_item
	return render(request,'front/index.html', data)
###########
#== Login ==#
def event_login(request):
	return render(request,'registration/login.html')
#== Signup ==#
def event_signup(request):
	return render(request,'registration/signup.html')
###########
#== Event ==#
def event(request):
	data = {}
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/event')
	else:
		form = EventForm()
	list_item = Event.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'admin/event.html', data)
def event_update(request, id):
	data = {}
	try:
		selected_item = Event.objects.get(pk=id)
		form = EventForm(instance=selected_item)
	except Event.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = EventForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/event')
	list_item = Event.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'admin/event.html',data)

def event_remove(request, id):
	data = {}
	try:
		selected_item = Event.objects.get(pk=id)
		selected_item.delete()
		form = Event()
	except Event.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = Event.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/event', data)
###########
#== User==#
def users(request):
	data = {}
	if request.method == 'POST':
		form = EventUsersForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/users')
	else:
		form = EventUsersForm()
	list_item = EventUsers.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(request, 'admin/users.html', data)

def users_update(request, id):
	data = {}
	try:
		selected_item = EventUsers.objects.get(pk=id)
		form = EventUsersForm(instance=selected_item)
	except EventUsers.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = EventUsersForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/users')
	list_item = EventUsers.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'admin/users.html',data)

def users_remove(request, id):
	data = {}
	try:
		selected_item = EventUsers.objects.get(pk=id)
		selected_item.delete()
		form = EventUsers()
	except EventUsers.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = EventUsers.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/users', data)
#== Group ==#
def groups (request):
	data = {}
	if request.method == 'POST':
		form = EventGroupsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/groups')
	else:
		form = EventGroupsForm()
	list_item = EventGroups.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(request, 'admin/groups.html', data)
def groups_update(request, id):
	data = {}
	try:
		selected_item = EventGroups.objects.get(pk=id)
		form = EventGroupsForm(instance=selected_item)
	except EventGroups.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = EventGroupsForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/groups')
	list_item = EventGroups.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'admin/groups.html',data)

def groups_remove(request, id):
	data = {}
	try:
		selected_item = EventGroups.objects.get(pk=id)
		selected_item.delete()
		form = EventGroups()
	except EventGroups.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = EventGroups.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/groups', data)