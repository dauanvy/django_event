from django.shortcuts import render

from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
from django.http import HttpResponseRedirect, Http404
from event.models import EventUsers, EventUsersForm
from event.models import EventGroups, EventGroupsForm
from event.models import Event, EventForm

def event_success(request):
	return render(request,'front/success.html')
def index(request):
	s = request.session.get('eventusers_id', None)
	data = {}
	list_item = Event.objects.all()
	data['list_item'] = list_item
	user = EventUsers.objects.filter(id=s)
	data['user']=user
	return render(request,'front/index.html', data)
###########
#== Login ==#
def event_login(request):
	s = request.session.get('eventusers_id',None)
	if s:
		return HttpResponseRedirect('/event')
	if request.method == 'POST':
		email = request.POST.get('email', None)
		password = request.POST.get('password', None)
		try:
			users = EventUsers.objects.get(email=email)
			if users.email == email and users.password == password:
				request.session['eventusers_id'] = users.id
				return HttpResponseRedirect('/event')
			else:
				return HttpResponseRedirect('/web/login')
		except Users.DoesNotExist:
			return HttpResponseRedirect('/web/login')
	return render(request,'registration/login.html')
#== Logout ==#
def event_logout(request):
	try:
		del request.session['eventusers_id']
	except KeyError:
		pass
	return render(request,'registration/login.html')
#== Signup ==#
def event_signup(request):
	s = request.session.get('eventusers_id', None)
	if not s:		
		data = {}
		if request.method == 'POST':
			form = EventUsersForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/web/success')
		else:
			form = EventUsersForm()
		list_item = EventUsers.objects.all()
		data['id'] = None
		data['list_item'] = list_item
		data['form'] = form
		return render(request,'registration/signup.html', data)
	else:
		return HttpResponseRedirect('/web/success')
###########
#== Event ==#
def event(request):
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
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
	user = EventUsers.objects.filter(id=s)
	data['user']=user
	return render(request,'admin/event.html', data)
def event_update(request, id):
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
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
	user = EventUsers.objects.filter(id=s)
	data['user']=user
	return render(request,'admin/event.html',data)

def event_remove(request, id):
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
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
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
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
	user = EventUsers.objects.filter(id=s)
	data['user']=user
	return render(request, 'admin/users.html', data)

def users_update(request, id):
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
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
	user = EventUsers.objects.filter(id=s)
	data['user']=user
	return render(request,'admin/users.html',data)

def users_remove(request, id):
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
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
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
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
	user = EventUsers.objects.filter(id=s)
	data['user']=user
	return render(request, 'admin/groups.html', data)
def groups_update(request, id):
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
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
	user = EventUsers.objects.filter(id=s)
	data['user']=user
	return render(request,'admin/groups.html',data)

def groups_remove(request, id):
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
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