from django.db import models

class Trips (models.Model):

    name = models.CharField(max_length=250)
    date = models.TextField()

    def __str__(self):
        return self.name