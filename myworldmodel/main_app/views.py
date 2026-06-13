from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Observation, Action
from .forms import ActionForm

def home(request):
    return HttpResponse('<h1>My World Model</h1>')

@login_required
def observations_index(request):
    observations = Observation.objects.all()
    return render(request, 'observations/index.html', {'observations': observations})

@login_required
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

@login_required
def add_action(request, observation_id):
    observation = Observation.objects.get(id=observation_id)
    # act on own only
    if observation.agent == request.user:
        form = ActionForm(request.POST)
        if form.is_valid():
            new_action = form.save(commit=False)
            new_action.observation_id = observation_id
            new_action.taken_at = timezone.now()
            new_action.save()
    return redirect('observation-detail', observation_id=observation_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('observation-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})


class ObservationCreate(LoginRequiredMixin, CreateView):
    model = Observation
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.agent = self.request.user
        form.instance.observed_at = timezone.now()
        return super().form_valid(form)


class ObservationUpdate(LoginRequiredMixin, CreateView):
    model = Observation
    fields = ['name', 'description']

    # write own only
    def get_queryset(self):
        return Observation.objects.filter(agent=self.request.user)


class ObservationDelete(LoginRequiredMixin, CreateView):
    model = Observation
    success_url = '/observations/'

    # write own only
    def get_queryset(self):
        return Observation.objects.filter(agent=self.request.user)


class ActionUpdate(LoginRequiredMixin, CreateView):
    model = Action
    fields = ['description']

    # write own only
    def get_queryset(self):
        return Action.objects.filter(observation__agent=self.request.user)


class ActionDelete(LoginRequiredMixin, DeleteView):
    model = Action

    def get_queryset(self):
        return Action.objects.filter(observation__agent=self.request.user)
    
    def get_success_url(self):
        return reverse('observation-detail', kwargs={'observation_id': self.object.observation.id})