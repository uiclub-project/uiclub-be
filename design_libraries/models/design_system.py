
from core.models import Auditor
from django.db import models


class DesignSystem(Auditor):
    description = models.TextField()
    company =  models.ForeignKey('Company', on_delete=models.CASCADE, related_name='design_systems')
    components = models.ManyToManyField('Component', related_name='design_systems')
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    
    @property
    def quantity_components(self):
        return self.components.count()
     
    def __str__(self):
        return self.name