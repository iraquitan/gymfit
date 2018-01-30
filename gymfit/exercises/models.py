from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Category(models.Model):
    """Model for exercise category."""
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Exercise(models.Model):
    """Model for exercise."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.IntegerField()
    reps = models.IntegerField()
    series = models.IntegerField()
    category = models.ForeignKey(Category, related_name='exercises',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name
