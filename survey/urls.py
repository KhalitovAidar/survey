from django.urls import path

from . import views
from .views import SurveyViewApi


urlpatterns = [
    path('', views.SurveyListView.as_view()),
    path('add_answer/<int:pk>', views.SurveyDetailView.as_view(), name='add_answer'),
    path('api/surveys/', SurveyViewApi.as_view()),
]

