from django.urls import path
from students import views

urlpatterns = [
    path('create-student/', views.StudentCreateView.as_view(), name='create_student'),
    path('list-of-students/', views.StudentListView.as_view(), name='list_of_students'),
    path('update-student/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete-student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student'),
    path('details-students/<int:pk>/', views.StudentDetailView.as_view(), name='details_students'),
    path('search/', views.search_navbar, name='search'),
    path('inactivate-student/<int:pk>/', views.inactivate_student, name='inactivate_student'),
    path('student-homework-list/', views.HomeworkListView.as_view(), name='student_homework_list'),
]