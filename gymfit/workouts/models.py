from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from gymfit.exercises.models import Exercise


class Workout(models.Model):
    """Model for Workout"""
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    creation_date = models.DateField(_('Creation date'), auto_now_add=True)
    comment = models.CharField(
        verbose_name=_('Description'), max_length=100, blank=True,
        help_text=_("A short description or goal of the workout. For "
                    "example 'Focus on back' or 'Week 1 of program xy'.")
    )
    user = models.ForeignKey(User, verbose_name=_('User'))


class WorkoutEntry(models.Model):
    """Model for WorkoutEntry"""
    workout = models.ForeignKey(Workout, verbose_name=_("Workout"))
    exercise = models.ForeignKey(Exercise, verbose_name=_("Exercise"))
    weight = models.IntegerField()
    reps = models.IntegerField()
    series = models.IntegerField()
