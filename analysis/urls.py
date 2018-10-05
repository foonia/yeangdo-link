from django.urls.conf import path

from . import views

urlpatterns = [
    path('', views.data_analysis, name='data_analysis'),
    path('info/', views.more_info, name='more_info'),
]
