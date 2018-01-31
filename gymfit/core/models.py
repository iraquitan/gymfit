from django.db import models
from django.utils.translation import ugettext_lazy as _


class RepetitionUnit(models.Model):
    """
    Setting unit, used in combination with an amount such as '10 reps', '5 km'
    """
    class Meta:
        ordering = ["name", ]

    name = models.CharField(max_length=100, verbose_name=_('Name'))

    def __str__(self):
        return self.name


class WeightUnit(models.Model):
    """
    Weight unit, used in combination with an amount such as '10 kg', '5 plates'
    """
    class Meta:
        ordering = ["name", ]

    name = models.CharField(max_length=100, verbose_name=_('Name'))

    def __str__(self):
        return self.name
