from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
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

class ObservationCreate(CreateView):
    model = Observation
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.observed_at = timezone.now()
        return super().form_valid(form)

class ObservationUpdate(UpdateView):
    model = Observation
    fields = ['name', 'description']

class ObservationDelete(DeleteView):
    model = Observation
    success_url = '/observations/'