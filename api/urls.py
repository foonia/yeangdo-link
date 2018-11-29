from django.urls import path
from django.conf.urls import re_path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'survey', views.SurveyViewSet)

urlpatterns = [
    path('bar/', views.bar_api_view, name='bar_api_view'),
    path('chart/', views.chart_api_view, name='chart_api_view'),
    path('curve/', views.curve_api_view, name='curve_api_view'),
    path('candle/', views.candle_api_view, name='candle_api_view'),

    re_path(r'^', include(router.urls)),
]

