from django.db import models

class Observation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    observed_at = models.DateTimeField()

    def __str__(self): # equivalent toString
        return self.name
