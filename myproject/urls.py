"""
URL configuration for myproject project.

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
from myproject import views

urlpatterns = [
    path('admin-panel/', admin.site.urls), #here site is a class of admin module and urls is a method of site class which is used to register the urls of the admin site
    path('about-us/',views.aboutUs,name='about-us'), #here we are passing the aboutUs view to the url which is present in the views.py file and we can access this view using the name 'about-us' in the template using {% url 'about-us' %} syntax
    path('contact/',views.courses,name='contact'),
    path('',views.homepage,name='homepage'), #here we are passing the homepage view to the url which is present in the views.py file and we can access this view using the name 'homepage' in the template using {% url 'homepage' %} syntax
    path('coursesdetails/',views.coursesdetails,name='coursesdetails'),
]
