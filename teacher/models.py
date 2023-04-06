from django.db import models

# Create your models here.

class Teacher(models.Model):

    school_subject = (('literature', 'Literature'), ('math', 'Math'), ('history', 'history'), ('biology', 'Biology'),
                      ('physiscs', 'Physics'), ('english', 'English'), ('geography', 'Geography'))
    school_level = (('primary', 'Primary'), ('gymnasium', 'Gymnasium'), ('highschool', 'Highschool'))

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    phone_number = models.CharField(max_length=14)
    education_level = models.CharField(max_length=50, choices=school_level)
    course = models.CharField(max_length=50, choices=school_subject)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'