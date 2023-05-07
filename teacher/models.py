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


class Homework(models.Model):

    homework_title = models.CharField(max_length=150)
    homework_description = models.TextField(max_length=2000)
    due_date = models.DateField()
    discipline = models.CharField(max_length=50, choices=Teacher.school_subject)
    classroom = models.ForeignKey('headmaster.Classroom', on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    image = models.ImageField(upload_to='images/', blank=True, null=True)
    file = models.FileField(upload_to='file/', blank=True, null=True)

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.homework_title}'