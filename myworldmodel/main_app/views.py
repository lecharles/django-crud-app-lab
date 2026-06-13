from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from .models import Observation
from .forms import ActionForm



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
    action_form = ActionForm()
    return render(request, 'observations/detail.html', {
        'observation': observation,
        'action_form': action_form,
    })

def add_action(request, observation_id):
    form = ActionForm(request.POST)
    if form.is_valid():
        new_action = form.save(commit=False)
        new_action.observation_id = observation_id
        new_action.taken_at = timezone.now()
        new_action.save()
    return redirect('observation-detail', observation_id=observation_id)

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