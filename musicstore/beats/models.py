from django.db import models

# Create your models here
class Producer(models.Model):
	username = models.CharField(max_length=25)
	phone = models.IntegerField()
	email = models.EmailField()

	def __str__(self):
		return self.username

class Beat(models.Model):
	name = models.CharField(max_length=25)
	category = models.CharField(max_length=35)
	playback = models.FileField(upload_to='media')
	producer = models.ForeignKey('Producer',on_delete=models.CASCADE)

	def __str__(self):
		return self.name
