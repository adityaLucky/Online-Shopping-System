from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(default='description default text')
	location = models.CharField(max_length=120, default='my location default')
	job = models.CharField(max_length=120, null=True)

	def __unicode__(self):
		return self.name