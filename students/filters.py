import django_filters
from django_filters import DateFilter

import students
from students import forms
from students.models import Student


class StudentFilter(django_filters.FilterSet):
    student_first_name = [(student.first_name, student.first_name.upper()) for student in
                          Student.objects.filter(active=True)]
    new = set(student_first_name)

    # first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    first_name = django_filters.ChoiceFilter(choices=new, label='First name')

    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')


class Meta:
    model = Student
    fields = ['first_name', 'last_name', 'age', 'email']


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.filters['first_name'].field.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Please enter first name'})
    self.filters['last_name'].field.widget.attrs.update(
        {'class': 'form-control', 'placeholder': 'Please enter last name'})
    self.filters['email'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter email'})
