from django.http import HttpResponse
from django.shortcuts import render

# from django.urls import path


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')


def sobre(request):
    return HttpResponse('Sobre')


def contato(request):
    return HttpResponse('Contato')
