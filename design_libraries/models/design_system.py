
from core.models import Auditor
from django.db import models


class DesignSystem(Auditor):
    
    class PopularityChoices(models.TextChoices):
        HIGH='High'
        MEDIUM='Medium'
        LOW='Low'
    large_description = models.TextField()
    short_description = models.TextField(default="Description here")
    company =  models.ForeignKey('Company', on_delete=models.CASCADE, related_name='design_systems')
    components = models.ManyToManyField('Component', related_name='design_systems')
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    popularity = models.CharField(
            max_length=10, 
            choices=PopularityChoices.choices,
            default=PopularityChoices.MEDIUM
        )
    thumbnail_image = models.ImageField(upload_to='thumbnails/')
    is_updated = models.BooleanField(default=True)
    slug = models.CharField(max_length=50)
    
    @property
    def quantity_components(self):
        return self.components.count()
     
    def __str__(self):
        return self.name