from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse('Тут будет размещаться информация про пункты приема лома')
