from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


# Own User model in case different fields want to be added later
class User(AbstractUser):
    is_manager = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


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
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    staff_asigned = models.ForeignKey("Staff_member", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.task_name} {self.task_description}'


class Staff_member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    name = models.CharField(max_length=30)  # Operations, Training, Sales, Other

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
