from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from headmaster.models import Classroom

# Create your views here.

class ClassroomCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'headmaster/create_classroom.html'
    model = Classroom
    fields = '__all__'
    success_url = reverse_lazy('list_of_classrooms')
    permission_required = 'headmaster.add_classroom'


class ClassroomListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'headmaster/list_of_classrooms.html'
    model = Classroom
    context_object_name = 'all_classrooms'
    permission_required = 'headmaster.view_list_of_classrooms'


class ClassroomUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'headmaster/update_classroom.html'
    model = Classroom
    fields = '__all__'
    success_url = reverse_lazy('list_of_classrooms')
    permission_required = 'headmaster.update_classroom'


class ClassroomDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'headmaster/delete_classroom.html'
    model = Classroom
    success_url = reverse_lazy('list_of_classrooms')
    permission_required = 'headmaster.delete_classroom'

@login_required()
@permission_required('headmaster.disable_classroom')
def inactivate_classroom(request, pk):
    Classroom.objects.filter(id=pk).update(active=False)

    return redirect('list_of_classrooms')