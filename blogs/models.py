from __future__ import unicode_literals

from django.template.defaultfilters import slugify
from django.db import models

import datetime

now = datetime.datetime.now()

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.name

class Blog(models.Model):
	category = models.ManyToManyField(Category)
	title = models.CharField(max_length=100, unique=True, default=None)
	author = models.CharField(max_length=100, null=True, blank=True, default=None)
	# COMPLETE
	slug = models.SlugField(null=True, blank=True, unique=True,  default=None, editable=False)
	photo = models.ImageField(upload_to='blogs', blank=True, default=None)
	content = models.TextField(default=None)
	published = models.BooleanField(default=True)
	date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date_published = models.DateTimeField(null=True, blank=True, editable=False)
	date_unpublished = models.DateTimeField(null=True, blank=True, editable=False)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		if(self.published):
			self.date_published = now
		if not self.published and self.date_added:
			self.date_unpublished = now
		super(Blog, self).save(*args, **kwargs)

	def listContent(self):
		count = 400
		content = self.content
		if(content > count):
			return content[:count]+"..."
		else:
			return self.content