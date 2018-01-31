from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect, Http404

def index(request):
	return render(request,'front/index.html')
def user_list(request):
	return render(request,'admin/user_list.html')
def user_form(request):
	return render(request,'admin/user_form.html')
