from django.db import models

class Project(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField('Tag', blank=True)
    featured_image=models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link=models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name