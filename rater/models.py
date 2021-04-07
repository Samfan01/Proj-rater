from django.db import models

# Create your models here.

class Project(models.Model):
    '''
    Project class to create instances of the project post
    '''
    title = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'rator/')
    description = models.TextField()
    link = models.URLField()
    
    def __str__(self):
        return self.title
        
    
    
    
