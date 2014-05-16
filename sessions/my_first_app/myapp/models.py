from django.db import models

# Create your models here.
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address=models.CharField(max_length=30)
	website=models.URLField(max_length=30)
	state_province=models.CharField(max_length=30)
	
	def _unicode_(self):
		return self.name






