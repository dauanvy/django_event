from django.db import models

# Create your models here.
from django import forms

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
	group = models.ManyToManyField(EventGroups, related_name="group_ids")
	class Meta:
		db_table = "eventusers"
		ordering = ['-id']
class EventUsersForm(forms.ModelForm):
	username = forms.CharField(label= 'User Name', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	password = forms.CharField(label= 'Password', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	repassword = forms.CharField(label= 'RePassword', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	email = forms.CharField(label= 'Email', max_length=100, strip=True, widget=forms.TextInput(attrs={'style':'width:100%'}))
	group = models.ManyToManyField(EventGroups)
	class Meta:
		model = EventUsers
		fields = ['username', 'password', 'repassword', 'email', 'group']
		widgets = {
			'body': forms.Textarea(),
			'group': forms.CheckboxSelectMultiple()
			}

