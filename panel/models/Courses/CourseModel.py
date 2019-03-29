from django.db import models
# from autoslug.fields import AutoSlugField
from django.contrib.auth.models import User
from panel.models.CategoryModels import Category

class Course(models.Model):
    def a(self,value):
        return(value.replace('-'))

    def b(self,instance):
        return(instance.title)

    title            = models.CharField(max_length=200)
    subtitle         = models.CharField(max_length=300)
    format           = models.CharField(max_length=200)
    summery          = models.TextField()
    speaker          = models.CharField(max_length=200)
    session          = models.IntegerField()
    holding_loc      = models.CharField(max_length=200)
    holding_date     = models.DateField(auto_now_add=True)
    audience         = models.CharField(max_length=200)
    scientific_level = models.CharField(max_length=200)
    prerequisite     = models.CharField(max_length=200)
    table_of_content = models.CharField(max_length=200)
    resources        = models.FileField(upload_to='document/Courses/resourses')
    category         = models.ForeignKey(Category, on_delete = models.CASCADE)
    image_index      = models.ImageField(upload_to='image/Courses/index', max_length=None)
    tags             = models.CharField(max_length=300)
    image_perview    = models.ImageField(upload_to='image/Courses/preview', max_length=None)
    

    # slug        = AutoSlugField(
    #                     populate_from = b,
    #                     unique_with=['title', 'pub_date'],
    #                     slugify = a)
    slug             = models.CharField(max_length=300)
    author           = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date         = models.DateTimeField(auto_now_add=True)
    update_date      = models.DateTimeField(auto_now_add=True)




