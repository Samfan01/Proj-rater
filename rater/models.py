from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile')
    bio = models.TextField()
    email = models.EmailField()
    
    @receiver(post_save, sender=User)
    def user_profile(sender,instance,created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
            
    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['email']
        
    def save_profile(self):
        self.save()
    
    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles
            
    


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
    
    class Meta:
        ordering = ['title']
        
    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects
    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects
    
    
