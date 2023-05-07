from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from teacher.forms import TeacherForm, TeacherUpdateForm, HomeworkForm, HomeworkUpdateForm
from teacher.models import Teacher, Homework

# Create your views here.

class TeacherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'teacher/create_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('list_of_teachers')
    permission_required = 'teacher.add_teacher'

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_teacher = form.save(commit=False)
            new_teacher.first_name = new_teacher.first_name.title()

            new_teacher.save()

        return redirect('homepage')


class TeacherListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'teacher/list_of_teachers.html'
    model = Teacher
    context_object_name = 'all_teachers'
    permission_required = 'teacher.view_list_of_teachers'

    def get_queryset(self):
        return Teacher.objects.filter(active=True)


class TeacherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'teacher/update_teacher.html'
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('list_of_teachers')
    permission_required = 'teacher.update_teacher'


class TeacherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'teacher/delete_teacher.html'
    model = Teacher
    success_url = reverse_lazy('list_of_teachers')
    permission_required = 'teacher.delete_teacher'

@login_required()
@permission_required('teacher.disable_teacher')
def inactivate_teacher(request, pk):
    Teacher.objects.filter(id=pk).update(active=False)

    return redirect('list_of_teachers')


class HomeworkCreateView(LoginRequiredMixin, CreateView):
    template_name = 'teacher/create_homework.html'
    model = Homework
    form_class = HomeworkForm
    success_url = reverse_lazy('list_of_homeworks')
    permission_required = 'teacher.create_homework'

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_homework = form.save(commit=False)
            new_homework.homework_title = new_homework.homework_title.title()

            new_homework.save()

        return redirect('list_of_homeworks')


class HomeworkListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'teacher/list_of_homeworks.html'
    model = Homework
    context_object_name = 'all_homeworks'
    permission_required = 'teacher.view_list_of_homeworks'

    def get_queryset(self):
        return Homework.objects.filter(active=True)

class HomeworkUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'teacher/update_homework.html'
    model = Homework
    form_class = HomeworkUpdateForm
    success_url = reverse_lazy('list_of_homeworks')
    permission_required = 'teacher.update_homework'


class HomeworkDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'teacher/delete_homework.html'
    model = Homework
    success_url = reverse_lazy('list_of_homeworks')
    permission_required = 'teacher.delete_homework'