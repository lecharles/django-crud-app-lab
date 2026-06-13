from django.contrib import admin
from .models import Observation, Action, Hypothesis

admin.site.register(Observation)
admin.site.register(Action)
admin.site.register(Hypothesis)