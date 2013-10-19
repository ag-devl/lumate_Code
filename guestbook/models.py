from django.db import models

# Create your models here.
class Visitor(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

def __unicode__(self):
	return self.first_name
