from django.shortcuts import render
from django.http import HttpResponse
from .models import Observation


def home(request):
    return HttpResponse('<h1>My World Model</h1>')

def observations_index(request):
    observations = Observation.objects.all()
    return render(request, 'observations/index.html', {'observations': observations})