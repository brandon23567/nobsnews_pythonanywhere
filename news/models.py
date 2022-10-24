from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	header_img = models.ImageField(upload_to='header_images/')
	snippet = models.TextField()
	body = RichTextField()
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

