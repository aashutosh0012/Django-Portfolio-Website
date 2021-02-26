from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	data = []
	context = {'data':data, 'data':data }
	return render(request,'resume/index.html', context)
