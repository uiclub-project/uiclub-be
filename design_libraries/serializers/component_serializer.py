from rest_framework import serializers
from design_libraries.models import  Component

class ComponentSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name', read_only=True)
    class Meta:
        model = Component
        fields = (
            'name',
            'description',
            'type',
            'company_name',
        )
