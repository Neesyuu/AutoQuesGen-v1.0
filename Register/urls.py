from django.contrib import admin
from django.urls import path
from Register import views

urlpatterns = [
    path('', views.registerView, name='registerView'),
]
