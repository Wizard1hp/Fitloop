from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),



   
]
