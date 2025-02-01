from rest_framework import generics
from design_libraries.serializers.component_serializer import ComponentSerializer
from design_libraries.models.component import Component

class ComponentDesignSystemsAPIView(generics.ListAPIView):
    serializer_class = ComponentSerializer

    def get_queryset(self):
        design_system_id = self.kwargs.get("design_id")
        return Component.objects.filter(design_systems__pk=design_system_id)