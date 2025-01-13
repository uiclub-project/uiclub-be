from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ArticleListAPIView.as_view(), name='article-list'),
]