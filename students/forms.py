from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Select, Textarea

from students.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            # 'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description',
                                           'rows': 3}),
            'gender': Select(attrs={'class': 'form-select'}),
            'current_class': Select(attrs={'class': 'form-select'}),

        }

    def clean(self):
        cleaned_data = self.cleaned_data  # stocam in variabila cleaned_data un dictionar cu valorile pe care le introduce utilizatorul in formular
        print(cleaned_data)

        all_students = Student.objects.filter(first_name__exact=cleaned_data.get(
            'first_name'))  # interogam tabela student_student si cautam daca exista un/mai multi studenti cu first_name identic
        if all_students:  # daca exista un student cu acelasi nume ne va genera o eroare
            msg = f'This first name {cleaned_data.get("first_name")} exists in database'  # mesajul erorii
            self._errors['first_name'] = self.error_class([msg])  # afisarea erorii

        all_emails = Student.objects.filter(email__exact=cleaned_data.get('email'))
        if all_emails:
            msg_email = f'This email {cleaned_data.get("email")} already exists'
            self._errors['email'] = self.error_class([msg_email])

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'description', 'gender', 'active', 'current_class']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            # 'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description',
                                           'rows': 3}),
            'gender': Select(attrs={'class': 'form-select'}),
            'current_class': Select(attrs={'class': 'form-select'}),

        }

    def clean(self):
        cleaned_data = self.cleaned_data  # stocam in variabila cleaned_data un dictionar cu valorile pe care le introduce utilizatorul in formular
        print(cleaned_data)

        all_students = Student.objects.filter(first_name__exact=cleaned_data.get(
            'first_name'))  # interogam tabela student_student si cautam daca exista un/mai multi studenti cu first_name identic
        if all_students:  # daca exista un student cu acelasi nume ne va genera o eroare
            msg = f'This first name {cleaned_data.get("first_name")} exists in database'  # mesajul erorii
            self._errors['first_name'] = self.error_class([msg])  # afisarea erorii

        all_emails = Student.objects.filter(email__exact=cleaned_data.get('email'))
        if all_emails:
            msg_email = f'This email {cleaned_data.get("email")} already exists'
            self._errors['email'] = self.error_class([msg_email])

        return cleaned_data