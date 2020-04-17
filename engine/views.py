from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from . import functions
# Create your views here.


def index(request):
	return render(request, 'chatengine/index.html')

def nahui(request: HttpRequest):
	return HttpResponse(f"Иди нахуй {request.get_host()}! Твои заголовки, пидр: {' '.join(request.headers.values())}")

def unauthorized(request: HttpRequest, chatid=None):
	if functions.is_registered():
		pass
		# направить на страницу комнаты, если она существует
	return HttpResponseRedirect(reverse('paradnoe'))


def paradnoe(request: HttpRequest):
	return HttpResponse("paradnoe")

def koridor(request: HttpRequest):
	return HttpResponse("koridor")

def palata(request, palata_name):
	return render(request, 'chatengine/palata.html', {
        'palata_name': palata_name
    })

def kuhnia(request: HttpRequest):
	return HttpResponse("Kuhnia")