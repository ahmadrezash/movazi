from django.db import models

class Category(models.Model):
    name_english = models.CharField(max_length = 100)
    name_persian = models.CharField(max_length = 100)
    description  = models.CharField(max_length = 300)
    
    # parent       =  models.ForeignKey('panel.Category', on_delete=models.CASCADE)

    create_date  = models.DateTimeField(auto_now_add=True)

