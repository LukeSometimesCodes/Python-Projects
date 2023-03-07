from django.db import models


# Create your models here.

class UniversityCampus(models.Model):
    title = models.CharField(max_length=60, default='', blank=True, null=False)
    state = models.CharField(max_length=2, default='', blank=True, null=False)
    campus_ID = models.IntegerField(default='', blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        return self.title
        # Returns the input value of the title and instructor name
        # field as the tuple to display in the browser instead of the default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    class Meta:
        verbose_name_plural = 'University Campus'
