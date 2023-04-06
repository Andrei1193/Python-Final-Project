from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.datetime_safe import datetime
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from students.filters import StudentFilter
from students.forms import StudentForm, StudentUpdateForm
from students.models import Student
from teacher.models import Teacher

class StudentCreateView(CreateView):
    template_name = 'students/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('homepage')
    # permission_required = 'students.add_student'

class StudentListView(ListView):
    template_name = 'students/list_of_students.html'
    model = Student
    context_object_name = 'all_students'  # Student.objects.all()
    # permission_required = 'students.view_list_of_students'


class StudentUpdateView(UpdateView):
    template_name = 'students/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list_of_students')
    # permission_required = 'students.update_student'


class StudentDeleteView(DeleteView):
    template_name = 'students/delete_student.html'
    model = Student
    success_url = reverse_lazy('list_of_students')
    # permission_required = 'students.can_delete_students'



class StudentDetailView(DetailView):
    template_name = 'students/details_students.html'
    model = Student

# @login_required()
def search_navbar(request):

    get_value = request.GET.get('search')

    if get_value:
        students = Student.objects.filter(Q(first_name__icontains=get_value) | Q(email__icontains=get_value))
    else:
        students = {}

    return render(request, 'students/search.html', {'allstudents': students})

# @login_required()
# @permission_required('student.disable_student')
def inactivate_student(request, pk):
    Student.objects.filter(id=pk).update(active=False)

    return redirect('list_of_students')