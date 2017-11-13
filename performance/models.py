"""
Performance models module
"""
from django.db import models
from actor.models import Actor


class Performance(models.Model):
    """
    Performance model
    """
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name="performance_actor")
    producer = models.ManyToManyField(Actor, related_name="performance_producer")
    duration = models.TimeField()
    sort_description = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """
        :return: performance name
        """
        return self.name
