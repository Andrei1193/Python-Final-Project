from django.urls import path

from proschool import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
]