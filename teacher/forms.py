from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Select, Textarea, DateInput, FileInput, SelectMultiple

from teacher.models import Teacher, Homework


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
            'education_level': Select(attrs={'class': 'form-select'}),
            'course': Select(attrs={'class': 'form-select'}),
            'image': FileInput(attrs={'class': 'form-control'}),

        }


class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your phone number'}),
            'education_level': Select(attrs={'class': 'form-select'}),

        }


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = '__all__'

        widgets = {
            'homework_title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your '
                                                                                       'homework title'}),
            'homework_description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your homework'
                                                                                            'description', 'rows': 3}),
            'due_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': FileInput(attrs={'class': 'form-control'}),
            'file': FileInput(attrs={'class': 'form-control'}),
        

        }


class HomeworkUpdateForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = '__all__'

        widgets = {
            'homework_title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your '
                                                                                       'homework title'}),
            'homework_description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your homework'
                                                                                            'description', 'rows': 3}),
            'due_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'image': FileInput(attrs={'class': 'form-control'}),
            'file': FileInput(attrs={'class': 'form-control'}),

        }
