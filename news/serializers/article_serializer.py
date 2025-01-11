from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'name',
            'title',
            'subtitle',
            'description',
            'autor',
            'content',
            'time_to_read',
            'slug',
            'category',
        )
    