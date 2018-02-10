from django.db import models

# Create your models here.
from django import forms
from datetime import date
from django.template.defaultfilters import slugify
#-------------------------- Authenticate ---------------------------------------#
#== Group ==#
class EventGroups(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=256, default='')
	class Meta:
		db_table = "eventgroups"
		ordering = ['-id']
	def __str__(self):
		return self.name
class EventGroupsForm(forms.ModelForm):
	name = forms.CharField(label= 'Name', max_length=100, strip=True)
	class Meta:
		model = EventGroups
		fields = ['name']

#== Users ==#		
class EventUsers(models.Model):
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=256, default='')
	password = models.CharField(max_length=256, default='')
	repassword = models.CharField(max_length=256, default='')
	email = models.CharField(max_length=256, default='')
	group = models.ManyToManyField(EventGroups, related_name="group_ids",blank=True, default=False)
	class Meta:
		db_table = "eventusers"
		ordering = ['-id']
	def __str__(self):
		return self.username
		
class EventUsersForm(forms.ModelForm):
	username = forms.CharField(label= 'User Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	password = forms.CharField(label= 'Password', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	repassword = forms.CharField(label= 'RePassword', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	email = forms.CharField(label= 'Email', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	group = models.ManyToManyField(EventGroups, blank=True)
	class Meta:
		model = EventUsers
		fields = ['username', 'password', 'repassword', 'email', 'group']
		widgets = {
			'body': forms.Textarea(),
			'group': forms.CheckboxSelectMultiple()
			}
#-------------------------- Event ---------------------------------------#
#== Category ==#
class EventCategory(models.Model):
	name = models.CharField(max_length=30)
	class Meta:
		db_table = "eventcategorys"
		ordering = ['-id']
	def __str__(self):
		return "%s" % (self.name)
		
class EventCategoryForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	class Meta:
		model = EventCategory
		fields = ['name']
#== Location ==#
class EventLocation(models.Model):
	name = models.CharField(max_length=30)
	street = models.CharField(max_length=30,default='')
	city = models.CharField(max_length=30,default='')
	country = models.CharField(max_length=30,default='')
	class Meta:
		db_table = "eventlocations"
		ordering = ['-id']
	def __str__(self):
		return "%s" % (self.name)
		
class EventLocationForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	street = forms.CharField(label='Street', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	city = forms.CharField(label='City', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	country = forms.CharField(label='Country', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	class Meta:
		model = EventLocation
		fields = ['name', 'street', 'city', 'country']
		
#== Event ==#
class Event(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(EventUsers, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
	name = models.CharField(max_length=256, default='')
	description = models.TextField(default= '')
	organizer = models.CharField(max_length=256, default='')
	phone = models.CharField(max_length=256, default='')
	category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True, blank=True)
	location = models.ForeignKey(EventLocation, on_delete=models.SET_NULL, null=True, blank=True)
	start_date = models.DateTimeField(null=True, blank=True)
	end_date = models.DateTimeField(null=True, blank=True)
	class Meta:
		db_table = "event"
		ordering = ['-id']
	def __str__(self):
		return self.name
class EventForm(forms.ModelForm):
	name = forms.CharField(label= 'Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	description = forms.CharField(label='Description', widget = forms.Textarea(attrs={'class':'form-control', 'rows':'20','id':'mytextarea',}))
	user = forms.ModelChoiceField(queryset=EventUsers.objects.all(), empty_label="----------")
	organizer = forms.CharField(label='Organizer', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))	
	phone = forms.CharField(label='Phone', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	start_date = forms.DateField(label='Start Date', input_formats = [ '%Y-%m-%d' ], required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	end_date = forms.DateField(label='End Date', input_formats = [ '%Y-%m-%d' ], required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	location = forms.ModelChoiceField(queryset=EventLocation.objects.all(), empty_label="----------")
	category = forms.ModelChoiceField(queryset=EventCategory.objects.all(), empty_label="----------")
	class Meta:
		model = Event
		fields = ['name', 'description', 'user' , 'phone', 'location','organizer','category', 'start_date', 'end_date']
		widgets = {
			'body': forms.Textarea(),
			}