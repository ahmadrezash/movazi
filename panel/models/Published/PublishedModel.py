from django.db import models
# from autoslug.fields import AutoSlugField
from django.contrib.auth.models import User
from panel.models.CategoryModels import Category

class Published(models.Model):
    def a(self,value):
        return(value.replace('-'))

    def b(self,instance):
        return(instance.title)

    title           = models.CharField(max_length=200)
    subtitle        = models.CharField(max_length=300)
    subject         = models.CharField(max_length=200) 
    summery         = models.TextField()
    full_text       = models.TextField()
    source          = models.URLField(
                      max_length=128, 
                      db_index=True, 
                      blank=True)
    publishing_date = models.DateField()
    category        = models.ForeignKey(Category, on_delete = models.CASCADE)
    image_index     = models.ImageField(upload_to='image/Published/index', max_length=None)
    image_cover     = models.ImageField(upload_to='image/Published/cover', max_length=None)
    author          = models.ForeignKey(User, on_delete = models.CASCADE)

    tags            = models.CharField(max_length=300)
    # slug        = AutoSlugField(
    #                     populate_from = b,
    #                     unique_with=['title', 'pub_date'],
    #                     slugify = a)
    slug        = models.CharField(max_length=300)
    pub_date    = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)




