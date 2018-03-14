from django import forms
from event.models import Event, Location, Category
import django_filters

class EventFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_expr='icontains')
	location = django_filters.ModelMultipleChoiceFilter(queryset=Location.objects.all(), widget=forms.CheckboxSelectMultiple)
	category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

	class Meta:
		model = Event
		fields = ['title','location','category']