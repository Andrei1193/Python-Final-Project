from django.db import models

from teacher.models import Teacher


# Create your models here.
class Classroom(models.Model):
    classroom_name = models.CharField(max_length=20)
    class_master = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.classroom_name