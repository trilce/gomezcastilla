from django.db import models
from django.template.defaultfilters import slugify


class Tag(models.Model):
	name = models.CharField(max_length=100,blank=True)
	
	def __unicode__(self):
		return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
		
    def __unicode__(self):
	    return self.name

class Post(models.Model):
	title =  models.CharField(max_length=100)
	content = models.TextField(blank=True)
	category = models.ForeignKey(Category)
	creation_date = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True)
	image = models.ImageField(upload_to='upload', verbose_name='image', blank=True)

	def __unicode__(self):
		return self.title

