from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('design-systems/', views.DesignSystemListAPIView.as_view(), name='design-system-list'),
]