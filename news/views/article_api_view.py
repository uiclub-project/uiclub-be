from news.serializers.article_serializer import ArticleSerializer
from rest_framework import generics


class ArticleAPIView(generics.ListAPIView):
  serializer_class = ArticleSerializer
