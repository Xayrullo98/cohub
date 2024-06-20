from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    client = models.CharField(max_length=50)
    date = models.DateField()
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to='media')
    picture2 = models.ImageField(upload_to='media',null=True,blank=True)
    picture3 = models.ImageField(upload_to='media',null=True,blank=True)
    text = models.TextField()
    auther = models.CharField(max_length=30,null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
