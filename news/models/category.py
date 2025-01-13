
from core.models import Auditor
from django.db import models


class Category(Auditor):
    class CategoryChoices(models.TextChoices):
        UX='UX Design'
        UI='UI Design'
        PRODUCT='Product Design'
        
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20, 
        choices=CategoryChoices.choices)