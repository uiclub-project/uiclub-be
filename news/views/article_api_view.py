from news.serializers.article_serializer import ArticleSerializer
from news.models import Article
from rest_framework import generics



class ArticleListAPIView(generics.ListAPIView):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  
class ArticleDetailAPIView(generics.RetrieveAPIView):   
    queryset = Article.objects.all()
    serializer_class= ArticleSerializer
    lookup_url_kwarg = 'article_id'