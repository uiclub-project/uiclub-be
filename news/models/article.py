
from core.models import Auditor
from django.db import models


class Article(Auditor):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    autor = models.CharField(max_length=255)
    content = models.TextField()
    time_to_read = models.IntegerField()
    slug= models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name