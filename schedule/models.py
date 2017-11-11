"""
Schedule models module
"""
from django.db import models
from performance.models import Performance


class Schedule(models.Model):
    """
    Schedule model
    """
    performance = models.ForeignKey(Performance)
    date_time = models.DateTimeField()
    place = models.CharField(max_length=255)
    ticket = models.URLField()

    def __str__(self):
        """
        :return: performance name
        """
        return self.performance.name
