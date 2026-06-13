from django.db import models
from django.urls import reverse

class Observation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    observed_at = models.DateTimeField()

    def __str__(self): # equivalent toString
        return self.name
    
    def get_absolute_url(self):
        return reverse('observation-detail', kwargs={'observation_id': self.id})
