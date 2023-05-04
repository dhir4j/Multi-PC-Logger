"""pc_logger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from pclogger.views import add_pc_info, search_pc, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pclogger/add_pc_info/', add_pc_info, name='add_pc_info'),
    path('', index, name='home'),
    path('search_pc/', search_pc, name='search_pc'),
]
