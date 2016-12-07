from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	name=models.CharField(max_length=100, default='1')
	author=models.CharField(max_length=100, default='1')

	def __str__(self):
		return self.name