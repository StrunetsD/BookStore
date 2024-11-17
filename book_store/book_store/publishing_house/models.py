from django.db import models

class PublishingHouse(models.Model):
    name = models.CharField(max_length=255)  
    founded_date = models.DateField(null=True, blank=True)  
    address = models.CharField(max_length=255, blank=True)  
    website = models.URLField(blank=True)  
    description = models.TextField(blank=True)  
    
    def __str__(self):
        return self.name