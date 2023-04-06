from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Course(models.Model):
    prefix = models.CharField(max_length=6)
    number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
    title = models.CharField(max_length=100)
    description = models.TextField()
    credit_hours = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)])

    def __str__(self):
        return self.prefix + " " + str(self.number) + ": " + self.title
        

class User(AbstractUser):
    pass
