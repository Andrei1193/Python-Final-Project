from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from headmaster.models import Classroom

# Create your views here.

class ClassroomCreateView(CreateView):
    template_name = 'headmaster/create_classroom.html'
    model = Classroom
    fields = '__all__'
    success_url = reverse_lazy('list_of_classrooms')


class ClassroomListView(ListView):
    template_name = 'headmaster/list_of_classrooms.html'
    model = Classroom
    context_object_name = 'all_classrooms'


class ClassroomUpdateView(UpdateView):
    template_name = 'headmaster/update_classroom.html'
    model = Classroom
    fields = '__all__'
    success_url = reverse_lazy('list_of_classrooms')


class ClassroomDeleteView(DeleteView):
    template_name = 'headmaster/delete_classroom.html'
    model = Classroom
    success_url = reverse_lazy('list_of_classrooms')


def inactivate_classroom(request, pk):
    Classroom.objects.filter(id=pk).update(active=False)

    return redirect('list_of_classrooms')