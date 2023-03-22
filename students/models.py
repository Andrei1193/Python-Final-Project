from django.db import models
from teacher.models import Teacher

# Create your models here.

class Classroom(models.Model):
    classroom_name = models.CharField(max_length=20)

    def __str__(self):
        return self.classroom_name


class Student(models.Model):

    gender_options = (('male', 'Male'), ('female', 'Female'))

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_id = models.IntegerField(unique=True)
    age = models.IntegerField
    email = models.EmailField(max_length=80)
    description = models.CharField(max_length=500)
    gender = models.CharField(max_length=10, choices=gender_options)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    current_class = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
