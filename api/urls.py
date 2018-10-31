from django.urls import path
from django.conf.urls import re_path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'survey', views.SurveyViewSet)

urlpatterns = [
    path('list/', views.SurveyListApiView.as_view(), name='SurveyListApiView'),
    re_path(r'^', include(router.urls)),
]

