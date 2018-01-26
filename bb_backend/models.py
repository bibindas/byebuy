from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	categories_name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.categories_name

class Item(models.Model):
	item_name = models.CharField(max_length=100) 
	category = models.ForeignKey(Category,on_delete=models.CASCADE)

	def __str__(self):
		return self.item_name

class Brand(models.Model):
	brand_name = models.CharField(max_length=50)
	brand_logo = models.ImageField(upload_to='brandlogo/')

	def __str__(self):
		return self.brand_name

class Image(models.Model):
	image = models.ImageField(upload_to='productimage/')


class Colour(models.Model):
	colour = models.CharField(max_length=50)	

	def __str__(self):
		return self.colour

class Product(models.Model):
	product_name = models.CharField(max_length=100)
	product_brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
	product_type = models.CharField(max_length=50)
	product_price = models.FloatField(null=True, blank=True, default=None)
	product_item = models.ForeignKey(Item,on_delete=models.CASCADE)
	product_image = models.ManyToManyField(Image)
	product_description = models.CharField(max_length=100)
	product_colour = models.ManyToManyField(Colour)

	def __str__(self):
		return self.product_name