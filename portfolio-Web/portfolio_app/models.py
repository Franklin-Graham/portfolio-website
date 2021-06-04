from django.db import models

# Create your models here.
class My_details(models.Model):
    Name = models.CharField(max_length=250)
    profile_image = models.ImageField(upload_to="pics")
    About = models.TextField()
    Resume_objective = models.TextField()
    contact = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    def __str__(self):
        return self.Name

class Project(models.Model):
    project_name = models.CharField(max_length=250)
    project_icon = models.ImageField(upload_to="pics")
    def __str__(self):
        return self.project_name

class Account(models.Model):
    Github = models.CharField(max_length=250)
    Twitter = models.CharField(max_length=250)
    Facebook = models.CharField(max_length=250)
    Instagram = models.CharField(max_length=250)
    Linkedln = models.CharField(max_length=250)
    Skype = models.CharField(max_length=250)
    Telegram = models.CharField(max_length=250)
    def __str__(self):
        return self.Github
