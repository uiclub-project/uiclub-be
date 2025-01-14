from core.models import Auditor
from django.db import models


class Company(Auditor):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name