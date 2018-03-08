from django.db import models

# Create your models here.
from django import forms
from django.template.defaultfilters import slugify

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
#==Category==
class Category(models.Model):
	name = models.CharField(max_length=30)
	class Meta:
		db_table = "categorys"
		ordering = ['-id']
	def __str__(self):
		return "%s" % (self.name)
		
class CategoryForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	class Meta:
		model = Category
		fields = ['name']
#==Location==
class Location(models.Model):
	name = models.CharField(max_length=30)
	street = models.CharField(max_length=30,default='')
	city = models.CharField(max_length=30,default='')
	country = models.CharField(max_length=30,default='')
	class Meta:
		db_table = "locations"
		ordering = ['-id']
	def __str__(self):
		return "%s" % (self.name)
		
class LocationForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	street = forms.CharField(label='Street', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	city = forms.CharField(label='City', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	country = forms.CharField(label='Country', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	class Meta:
		model = Location
		fields = ['name', 'street', 'city', 'country']		
#== Event ==#
class Event(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(EventUsers, on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
	name = models.CharField(max_length=256, default='')
	title = models.TextField(default='')
	description = models.TextField(default='')
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
	start_date = models.DateTimeField(null=True, blank=True)	
	organizer = models.CharField(max_length=256, default='')
	phone = models.CharField(max_length=256, default='')
	slug = models.SlugField(default='')
		
	def __unicode__(self):
		return '%s' % self.title

	def get_absolute_url(self):
		return "/detail/%s/" % (self.slug)

	def save(self):
		self.slug = slugify(self.title)
		super(Event,self).save()

	class Meta:
		db_table = "event"
		ordering = ['-id']
	
class EventForm(forms.ModelForm):
	name = forms.CharField(label= 'Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))	
	user = forms.ModelChoiceField(queryset=EventUsers.objects.all(), empty_label="----------")
	organizer = forms.CharField(label='Organizer', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))	
	phone = forms.CharField(label='Phone', required=False, widget=forms.TextInput(attrs={'style':'width:100%'}))
	start_date = forms.DateField(label='Start Date', required=False, input_formats = [ '%Y-%m-%d' ], widget=forms.TextInput(attrs={'style':'width:100%'}))
	location = forms.ModelChoiceField(queryset=Location.objects.all(), empty_label="----------")
	category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="----------")
	title = forms.CharField(label= 'Title', widget = forms.Textarea(attrs={'class':'form-control', 'rows':'5','id':'titletextarea',}))
	description = forms.CharField(label= 'Description', widget = forms.Textarea(attrs={'class':'form-control', 'rows':'20','id':'destextarea',}))
	class Meta:
		model = Event
		fields = ['name', 'description', 'user','title', 'phone', 'location','organizer','category', 'start_date']
		widgets = {
			'body': forms.Textarea()
			}