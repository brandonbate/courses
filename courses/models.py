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
    
class Term(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
class CourseInstance(models.Model):
    # on_delete=models.PROTECT prevents Academic Terms from being deleted.
    term = models.ForeignKey('Term', on_delete=models.PROTECT) 
    course = models.ForeignKey('Course', on_delete=models.PROTECT)
    section = models.CharField(max_length=6)
    location = models.CharField(max_length=100)
    class_time = models.CharField(max_length=100)

    def __str__(self):
        return str(self.term) + ", " + str(self.course) + " " + str(self.section)

# Records which faculty are instructors for a course instance. This structure
# allows for faculty to team teach a course.
class CourseInstanceInstructor(models.Model):
    course_instance = models.ForeignKey('CourseInstance', on_delete=models.PROTECT)
    instructor = models.ForeignKey('User', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.instructor) + " " + str(self.course_instance)

# Records which students are enrolled in a course instance.
class CourseInstanceStudent(models.Model):
    course_instance = models.ForeignKey('CourseInstance', on_delete=models.PROTECT)
    student = models.ForeignKey('User', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.student) + " " + str(self.course_instance)

class User(AbstractUser):
    def __str__(self):
        return str(self.last_name + ", " + self.first_name)
