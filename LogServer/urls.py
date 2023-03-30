# File name: LogServer/urls.py
from django.contrib import admin
from django.urls import path, include  # Add include here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pclogger/', include('pclogger.urls')),  # Add this line to include the app's URLs
]
