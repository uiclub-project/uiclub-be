
from core.models import Auditor
from django.db import models


class Component(Auditor):
    
    "image needed pending"
    class ComponentChoices(models.TextChoices):
        FORM='Form'
        INPUT='Input'
            
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(
            max_length=10, 
            choices=ComponentChoices.choices,
        )
    company =  models.ForeignKey('Company', on_delete=models.CASCADE)
       
    def __str__(self):
        return self.name