from django.db import models

# Create your models here.
class Page(models.Model):
	item_name = models.CharField(max_length=255)
	price = models.CharField(max_length=255)
	image = models.ImageField(default='/image')
	date = models.DateTimeField()

	def __str__(self):
		return self.item_name