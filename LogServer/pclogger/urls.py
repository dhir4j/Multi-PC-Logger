# File name: pclogger/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_pc_info/', views.log_pc_data, name='log_pc_data'),
]
