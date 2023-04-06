from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from teacher.forms import TeacherForm, TeacherUpdateForm
from teacher.models import Teacher

# Create your views here.

class TeacherCreateView(CreateView):
    template_name = 'teacher/create_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('homepage')
    # permission_required = 'teacher.add_teacher'

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_teacher = form.save(commit=False)
            new_teacher.first_name = new_teacher.first_name.title()

            new_teacher.save()

        return redirect('homepage')


class TeacherListView(ListView):
    template_name = 'teacher/list_of_teachers.html'
    model = Teacher
    context_object_name = 'all_teachers'
    # permission_required = 'teacher.view_list_of_teachers'

    def get_queryset(self):
        return Teacher.objects.filter(active=True)


class TeacherUpdateView(UpdateView):
    template_name = 'teacher/update_teacher.html'
    model = Teacher
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('list_of_teachers')
    # permission_required = 'teacher.update_teacher'


class TeacherDeleteView(DeleteView):
    template_name = 'teacher/delete_teacher.html'
    model = Teacher
    success_url = reverse_lazy('list_of_teachers')
    # permission_required = 'teacher.delete_teacher'

# @login_required()
# @permission_required('trainer.disable_trainer')
def inactivate_teacher(request, pk):
    Teacher.objects.filter(id=pk).update(active=False)

    return redirect('list_of_teachers')