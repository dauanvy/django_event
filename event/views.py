from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password

from event.filters import EventFilter
# Create your views here.
from django.http import HttpResponseRedirect, Http404
from event.models import EventUsers, EventUsersForm
from event.models import EventGroups, EventGroupsForm
from event.models import Event, EventForm
from event.models import Location, LocationForm
from event.models import Category, CategoryForm

def event_success(request):
	return render(request,'front/success.html')
def index(request):
	s = request.session.get('eventusers_id', None)
	data = {}
	list_item = Event.objects.all()
	data['list_item'] = list_item
	user = EventUsers.objects.filter(id=s)
	data['user']=user
	#filter
	event_filter = EventFilter(request.GET, queryset=list_item)
	data['filter']=event_filter
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
			try:
				users = EventUsers.objects.get(email=email)
				if users.email == email and users.password == password:
					request.session['eventusers_id'] = users.id
					return HttpResponseRedirect('/event')
				else:
					return HttpResponseRedirect('/web/login')
			except ObjectDoesNotExist:
				content = None
			
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
#category
def category(request):
	form = CategoryForm(request.POST)
	data = {}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/category')
	else :
		form = CategoryForm()
	list_item = Category.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'admin/category.html',data)
def category_update(request, id):
	data = {}
	try:
		selected_item = Category.objects.get(pk=id)
		form = CategoryForm(instance=selected_item)
	except Category.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = CategoryForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/category')
	list_item = Category.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'admin/category.html',data)
def category_remove(request, id):
	data = {}
	try:
		selected_item = Category.objects.get(pk=id)
		selected_item.delete()
		form = Category()
	except Category.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = Category.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/category', data)
#Location
def location(request):
	form = LocationForm(request.POST)
	data = {}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/location')
	else :
		form = LocationForm()
	list_item = Location.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'admin/location.html',data)
def location_update(request, id):
	data = {}
	try:
		selected_item = Location.objects.get(pk=id)
		form = LocationForm(instance=selected_item)
	except Location.DoesNotExist:
		raise Http404("This item not exist.")
	if request.method == 'POST':
		form = LocationForm(request.POST or None, instance=selected_item)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/location')
	list_item = Location.objects.all()
	data['id'] = id
	data['list_item'] = list_item
	data['form'] = form
	return render(request,'admin/location.html',data)
def location_remove(request, id):
	data = {}
	try:
		selected_item = Location.objects.get(pk=id)
		selected_item.delete()
		form = LocationForm()
	except Location.DoesNotExist:
		raise Http404("This item not exist.")
	list_item = Location.objects.all()
	data['id'] = None
	data['list_item'] = list_item
	data['form'] = form
	return HttpResponseRedirect('/location', data)
#== Event ==#
def event_list(request):
	s = request.session.get('eventusers_id', None)
	data = {}
	list_item = Event.objects.all()
	data['list_item'] = list_item
	user = EventUsers.objects.filter(id=s)
	data['user']=user
	return render(request,'admin/event_list.html', data)	
def event(request):	
	s = request.session.get('eventusers_id', None)
	if not s:
		return HttpResponseRedirect('/web/login')
	form = EventForm(request.POST)
	data = {}
	if request.method == 'POST':
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
	return HttpResponseRedirect('/event_list', data)
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

#== Search event ==
# def search(request):
    # event_list = Event.objects.all()
    # event_filter = EventFilter(request.GET, queryset=event_list)
    # return render(request, 'search/event_list.html', {'filter': event_filter})