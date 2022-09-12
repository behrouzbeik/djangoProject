from django.db import models
from django.urls import reverse

# Create your models here.

class MenuItems(models.Model):
    EnCaption = models.CharField(max_length=50)
    DeCaption = models.CharField(max_length=50)
    Url = models.CharField(max_length=100)

    def __str__(self):
        return self.EnCaption

class Category(models.Model):
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub')
    sub_cat = models.BooleanField(default=False)
    EnName = models.CharField(max_length=100)
    DeName = models.CharField(max_length=100)
    Fontawesome4 = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(upload_to='Services',blank=True,null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True , unique=True,blank=True,null=True)

    def __str__(self):
        return self.EnName

    def get_absoloute_url(self):
        return reverse('home:category' ,args=[self.slug,self.id])