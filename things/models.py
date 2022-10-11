from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Thing(models.Model):
    # Create a name field which cannot be blank, must be unique, and have a length of 30 characters or less
    name = models.CharField(max_length=30, unique=True, blank=False)
    # Create a description field which can be blank, but has a length of 120 characters or less
    description = models.CharField(max_length=120, blank=True)
    # Create a quantity field which can be a value between 0 and 100 (inclusive)
    quantity = models.IntegerField(default=0, blank=False, null=False, validators=[MinValueValidator(0), MaxValueValidator(100)])
