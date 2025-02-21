from core.models import Auditor
from django.db import models


class Link(Auditor):
    figma =  models.URLField(null=True)
    web =  models.URLField(null=True) 
    storybook = models.URLField(null=True) 
    