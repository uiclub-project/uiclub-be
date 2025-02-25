from django.urls import path
from . import views

urlpatterns = [
    path('design-systems/', views.DesignSystemListAPIView.as_view(), name='design-system-list'),
    path('design-systems/<slug:slug>/', views.DesignSystemDetailAPIView.as_view(), name='design-system-list'),
    path("design-systems/<int:design_id>/components/", views.ComponentDesignSystemsAPIView.as_view(), name="design-components"),
    path("design-systems/component/<int:component_id>/", views.ComponentDetailAPIView.as_view(), name="component"),
]