from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('quiz_detail/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz_detail/<int:quiz_id>/save/', views.saveq, name='saveq'),
]