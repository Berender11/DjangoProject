from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('survey/', views.survey_view, name='survey'),
]