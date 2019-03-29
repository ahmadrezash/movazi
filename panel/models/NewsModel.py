from django.db import models
# from autoslug.fields import AutoSlugField
from django.contrib.auth.models import User

class News(models.Model):
    def a(self,value):
        return(value.replace('-'))

    def b(self,instance):
        return(instance.title)

    title       = models.CharField(max_length=200)
    subtitle    = models.CharField(max_length=300)
    summery     = models.TextField()
    full_text   = models.TextField()
    # slug        = AutoSlugField(
    #                     populate_from = b,
    #                     unique_with=['title', 'pub_date'],
    #                     slugify = a)
    slug        = models.CharField(max_length=300)
    image       = models.ImageField(upload_to='image/News', max_length=None)
    author      = models.ForeignKey(User, on_delete = models.CASCADE)
    tags        = models.CharField(max_length=300)
    pub_date    = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)




