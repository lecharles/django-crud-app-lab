from django.shortcuts import render
from django.http import HttpResponse
from .models import Observation


def home(request):
    return HttpResponse('<h1>My World Model</h1>')

def observations_index(request):
    observations = Observation.objects.all()
    return render(request, 'observations/index.html', {'observations': observations})

def observations_detail(request, observation_id):
    try:
        observation = Observation.objects.get(id=observation_id)
    except Observation.DoesNotExist:
        raise Http404('Observation does not exist')
    return render(request, 'observations/detail.html', {'observation': observation})