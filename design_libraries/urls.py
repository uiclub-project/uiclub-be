from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('design_systems/', views.DesignSystemListAPIView.as_view(), name='design-system-list'),
]