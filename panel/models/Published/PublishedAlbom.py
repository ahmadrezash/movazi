from django.db import models
from panel.models.Published.PublishedModel import Published

class PublishedAlbum(models.Model):
    def a(self,value):
        return(value.replace('-'))

    def b(self,instance):
        return(instance.title)
    publish     = models.ForeignKey(Published,on_delete = models.CASCADE)
    image       =models.ImageField(upload_to='image/Published/Album', max_length=None)
    slug        = models.CharField(max_length=300)
    pub_date    = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)




