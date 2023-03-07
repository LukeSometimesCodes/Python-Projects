from django.db import models
from django.db.models import IntegerField


# Create your models here.

class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default='', blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default='', blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        return self.title


    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = 'University Classes'
