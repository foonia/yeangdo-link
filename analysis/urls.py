from django.urls.conf import path

from . import views


app_name = 'analysis'

urlpatterns = [
    path('', views.index, name='index'),
    path('plot/', views.show_plot, name='show_plot'),
    path('submit/', views.submit_data, name='submit_data'),
    # path('info/', views.data, name='more_info'),
]
