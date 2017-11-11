"""
Actor models module
"""
from django.db import models


class Actor(models.Model):
    """
    Actor model
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='photos/',)

    def __str__(self):
        """
        :return: actor full name
        """
        return '{} {}'.format(self.first_name, self.last_name)
