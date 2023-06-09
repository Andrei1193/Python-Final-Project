from django.urls import path
from userextend import views


urlpatterns = [
    path('create-user/', views.UserExtendCreateView.as_view(), name='create_user'),
    path('activate_user/<int:pk>/<str:token>/', views.activate_user, name='activate-user')

]