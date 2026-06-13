from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Observation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    observed_at = models.DateTimeField()
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    hypotheses = models.ManyToManyField('Hypothesis')

    def __str__(self): # equivalent toString
        return self.name
    
    def get_absolute_url(self):
        return reverse('observation-detail', kwargs={'observation_id': self.id})

class Action(models.Model):
    description = models.TextField()
    taken_at = models.DateTimeField()
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('observation-detail', kwargs={'observation_id': self.observation.id})

class Hypothesis(models.Model):
    STATUSES = [
        ('open', 'Open'),
        ('supported', 'Supported'),
        ('refuted', 'Refuted'),
        ('inconclusive', 'Inconclusive'),
    ]
    statement = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUSES, default='open')
    created_at = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Hypotheses' # Django docs option that sets a model's plural name

    def __str__(self):
        return self.statement