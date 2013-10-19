from django.db import models

# Create your models here.
class Visitor(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
        visited_on = models.DateTimeField('date visited')

def __unicode__(self):
	return "%s %s %r" %(self.first_name, self.last_name, self.visited_on)
