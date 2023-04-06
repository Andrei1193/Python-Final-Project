from django.urls import path
from teacher import views

urlpatterns = [
    path('create-teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),
    path('list-of-teachers/', views.TeacherListView.as_view(), name='list_of_teachers'),
    path('update-teacher/<int:pk>/', views.TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete-teacher/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete_teacher'),
    path('inactivate-teacher/<int:pk>/', views.inactivate_teacher, name='inactivate_teacher'),
]
