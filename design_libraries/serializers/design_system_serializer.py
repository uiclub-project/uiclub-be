from rest_framework import serializers
from design_libraries.models import DesignSystem
from design_libraries.serializers.component_serializer import ComponentSerializer

class DesignSystemSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True, read_only=True)
    class Meta:
        model = DesignSystem
        fields = (
            'id',
            'description',
            'company',
            'components',
            'name',
            'version',
            'quantity_components',
        )
    