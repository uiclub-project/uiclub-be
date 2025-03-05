from rest_framework import generics, filters
from design_libraries.models import DesignSystem
from design_libraries.serializers.design_system_serializer import DesignSystemListSerializer, DesignSystemDetailSerializer


class DesignSystemListAPIView(generics.ListAPIView):
  queryset = DesignSystem.objects.prefetch_related('company')
  serializer_class = DesignSystemListSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['name']

class DesignSystemDetailAPIView(generics.RetrieveAPIView):
  queryset = DesignSystem.objects.prefetch_related('components__company')  
  serializer_class = DesignSystemDetailSerializer
  lookup_field = 'slug' 
  lookup_url_kwarg = 'slug'  
#todo: components api view pending