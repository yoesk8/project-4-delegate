from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


# Own User model in case different fields want to be added later
class User(AbstractUser):
    pass


class Task(models.Model):
    # This tuple is the different departments that gets passed to the
    # department variable
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
    staff_asigned = models.ForeignKey("Staff_member", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task_name} {self.task_description}'


class Staff_member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
