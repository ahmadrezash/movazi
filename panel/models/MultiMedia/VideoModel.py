from django.db import models
# from autoslug.fields import AutoSlugField
from django.contrib.auth.models import User
from panel.models.CategoryModels import Category


class Video(models.Model):
	def a(self, value):
		return (value.replace('-'))

	def b(self, instance):
		return (instance.title)

	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=300)
	discription = models.TextField()
	# slug        = AutoSlugField(
	#                     populate_from = b,
	#                     unique_with=['title', 'pub_date'],
	#                     slugify = a)
	slug = models.CharField(max_length=300)
	image = models.ImageField(upload_to='images', max_length=None, name='تصویر')
	file = models.FileField(upload_to='video', max_length=None)
	preview_img = models.ImageField(upload_to='image/preview/video', max_length=None)
	url = models.URLField(max_length=250)

	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	time = models.IntegerField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.CharField(max_length=300)
	pub_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now_add=True)
