from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Task(models.Model):

    DEPARTMENT = (
       ('Operations', 'Operations'),
       ('FOH', 'FOH'),
       ('Sales', 'Sales')
    )
    
    task_name = models.CharField(max_length=100)
    task_description = models.CharField(max_length=1000)
    department = models.CharField(choices=DEPARTMENT, max_length=100)
    task_priority = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    task_picture = models.ImageField(blank=True, null=True)
    needed_files = models.FileField(blank=True, null=True)
