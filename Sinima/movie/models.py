from django.db import models
# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length = 180)
	year = models.IntegerField()
	source = models.FileField()
	def __str__(self):
		return self.title + "  " + str(self.year)
