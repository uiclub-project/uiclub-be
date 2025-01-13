from news.serializers.article_serializer import ArticleSerializer
from news.models import Article
from rest_framework import generics



class ArticleListAPIView(generics.ListAPIView):
  serializer_class = ArticleSerializer
  queryset = Article.objects.all()
  

