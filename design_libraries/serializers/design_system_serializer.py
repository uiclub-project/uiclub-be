from rest_framework import serializers
from design_libraries.models import DesignSystem
from design_libraries.serializers.component_serializer import ComponentSerializer
from design_libraries.serializers.link_serializer import LinkSerializer

class DesignSystemListSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = DesignSystem
        fields = (
            'id',
            'short_description',
            'company_name',
            'name',
            'quantity_components',
            'popularity',
            'is_updated',
            'thumbnail_image',
            'slug'
        )
        
        
class DesignSystemDetailSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True, read_only=True)
    links= LinkSerializer(read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = DesignSystem
        fields = (
            'id',
            'large_description',
            'company_name',
            'name',
            'version',
            'quantity_components',
            'popularity',
            'is_updated',
            'components',  
            'thumbnail_image',
            'links'
        )