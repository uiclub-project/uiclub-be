from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListAPIView.as_view(), name='article-list'),
    path('articles/<int:article_id>/', views.ArticleDetailAPIView.as_view(), name='article-detail'),   
]