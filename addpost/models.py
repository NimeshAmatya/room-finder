from django.db import models

# Create your models here.

class Room(models.Model):
	pdf = models.ImageField(upload_to = "room/pdfs")
	location = models.TextField()
	description = models.TextField()
	price = models.IntegerField()

	def __str__(self):
		return self.location

