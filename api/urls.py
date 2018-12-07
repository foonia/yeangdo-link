from django.urls import path
from django.conf.urls import re_path, include

from . import views


urlpatterns = [
    path('survey/', views.SurveyListApiView.as_view(), name='survey_list_api_view'),
    path('bar/', views.bar_api_view, name='bar_api_view'),
    path('chart/', views.chart_api_view, name='chart_api_view'),
    path('curve/', views.curve_api_view, name='curve_api_view'),
    path('candle/', views.candle_api_view, name='candle_api_view'),
]

