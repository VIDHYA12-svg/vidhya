"""vidhyasonlinsales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('validate/',views.Validate,name="validate"),
    path('addmerchant/',views.addmerchant,name="addmerchant"),
    path('viewmerchant/',views.viewmerchant,name="viewmerchant"),
    path('deletemerchant/',views.deletemerchant,name="deletemerchant"),
    path('addmrc/',views.addmrc,name="addmrc"),
    path('delmerc/',views.deletemerchant,name="delmerc"),
    path('writeone/',views.Writeone.as_view(),name="writeone"),
    path('readone/',views.Readone.as_view(),name="readone"),
    path('addproduct/',views.Addproduct.as_view(),name="addproduct"),
    path('changepwd/',views.Changepwd.as_view(),name="changepwd")

]
