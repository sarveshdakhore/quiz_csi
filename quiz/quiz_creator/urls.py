from django.urls import path
from . import views

urlpatterns = [
    path('check_quiz_name/', views.check_quiz_name, name='check_quiz_name'),
    path('create_quiz/', views.create_quiz, name='create_quiz'),
]