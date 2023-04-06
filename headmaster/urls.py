from django.urls import path
from headmaster import views

urlpatterns = [
    path('create-classroom/', views.ClassroomCreateView.as_view(), name='create_classroom'),
    path('list-of-classrooms/', views.ClassroomListView.as_view(), name='list_of_classrooms'),
    path('update-classroom/<int:pk>/', views.ClassroomUpdateView.as_view(), name='update_classroom'),
    path('delete-classroom/<int:pk>/', views.ClassroomDeleteView.as_view(), name='delete_classroom'),
    path('inactivate-classroom/<int:pk>/', views.inactivate_classroom, name='inactivate_classroom'),
]