import uuid

from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Muscle(models.Model):
    """Model for Muscle"""
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    is_front = models.BooleanField(default=1)

    class Meta:
        ordering = ["name", ]

    def __str__(self):
        return self.name


class Equipment(models.Model):
    """Model for Equipment"""
    name = models.CharField(max_length=100, verbose_name=_("Name"))

    def __str__(self):
        return self.name


class Category(models.Model):
    """Model for exercise category."""
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField()

    class Meta:
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Exercise(models.Model):
    """Model for exercise."""
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(max_length=2000,
                                   verbose_name=_('Description'),
                                   validators=[MinLengthValidator(30)])
    category = models.ForeignKey(Category, models.SET_NULL, blank=True,
                                 null=True, verbose_name=_("Category"))
    muscles = models.ManyToManyField(Muscle, blank=True,
                                     verbose_name=_('Primary muscles'))
    muscles_secondary = models.ManyToManyField(
        Muscle, verbose_name=_('Secondary muscles'),
        related_name='secondary_muscles', blank=True)
    equipment = models.ManyToManyField(Equipment, verbose_name=_('Equipment'),
                                       blank=True)
    creation_date = models.DateField(_('Date'), auto_now_add=True, null=True,
                                     blank=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False, verbose_name='UUID')

    class Meta:
        ordering = ["name", ]

    def __str__(self):
        return self.name
