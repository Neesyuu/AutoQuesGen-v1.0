from django.contrib import admin
from django.urls import path
from Dashboard import views

urlpatterns = [
    path('', views.dashboardView, name='dashboardView'),
]
