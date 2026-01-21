"""
URL configuration for Project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homepage,name='Homepage'),
    
    
    # Inster data into DEPT table
    path("insert_dept/", insert_dept, name="insert_dept"),
    
    # Display data from DEPT table
    path("Display_dept/", Display_dept, name="Display_dept"),
    
    # Inster data into EMP table
    
    path("insert_emp/", insert_emp, name="insert_emp"),
    
    # Display data from EMP table
    
    path("Display_emp/", Display_emp, name="Display_emp"),
]
