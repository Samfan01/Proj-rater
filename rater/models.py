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
    post_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    
    
