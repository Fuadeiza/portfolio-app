from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserPortfolio(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='userportfolio')
    bio= models.CharField(max_length=50, blank=True,null=True)
    phone_number = PhoneNumberField(unique=True, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank= True, null=True)
    twitter_username= models.CharField(max_length=50, blank=True,null=True)
    facebook_username= models.CharField(max_length=50, blank=True,null=True)
    linkedin_username= models.CharField(max_length=50, blank=True,null=True)
    github_username= models.CharField(max_length=50, blank=True,null=True)

    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('PortfolioApp:list')

    def __str__(self):
        return self.user.username


class UserProject(models.Model):
    user=models.OneToOneField(UserPortfolio, on_delete=models.CASCADE)
    project_name= models.CharField(max_length= 150)
    project_description=models.TextField()
    link=models.URLField(blank=True,help_text="Please enter the URL of your project page.")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('PortfolioApp:userprofile.html')

    def __str__(self):
        return self.project_name

@receiver (post_save, sender=User)
def create_userprofile(sender, instance, created ,**kwargs):
    if created:
        UserPortfolio.objects.create(user=instance)

@receiver (post_save, sender=User)
def save_userprofile(sender, instance, created, **kwargs):
    instance.userportfolio.save()

@receiver (post_save, sender=UserPortfolio)
def create_userproject(sender, instance, **kwargs):
    if True:
        UserProject.objects.create(user=instance)

@receiver (post_save, sender=UserPortfolio)
def save_userproject(sender, instance, created, **kwargs):
    instance.userproject.save()
    
