from django.shortcuts import render, render_to_response, HttpResponse
from add.models import numbers
import datetime

def home(request):
	return render(request, 'home.html')
def addition(request):
	num_1 = int(request.POST.get('num1'))
	num_2 = int(request.POST.get('num2'))
	# num = int(num_1)+int(num_2)
	num = num_1+num_2
	return HttpResponse(num)
