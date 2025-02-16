from rest_framework import serializers
from design_libraries.models import  Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            'storybook',
            'figma',
            'web',
        )
