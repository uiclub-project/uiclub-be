
from rest_framework import generics
from design_libraries.models import DesignSystem
from design_libraries.serializers.design_system_serializer import DesignSystemSerializer


class DesignSystemListAPIView(generics.ListAPIView):
  queryset = DesignSystem.objects.prefetch_related('components', 'company')
  serializer_class = DesignSystemSerializer
  