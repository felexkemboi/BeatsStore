from django.db import models

# Create your models here
class Producer(models.Model):
	username = models.CharField(max_length=25)
	phone = models.IntegerField()
	email = models.EmailField()

	def __str__(self):
		return self.username




CHOICES=(
	        ('BONGO','bongo'),
        	('GOSPEL', 'gospel'),
        	('REGGAE', 'reggae'),
        	('HIPHOP', 'hiphop'),
        	('BLUES', 'blues'),
        	('R & B', 'r & b'),
       		('ROCK', 'rock'),
			('SOUND TRACK', 'sound_track'),
    )

class Beat(models.Model):
	name = models.CharField(max_length=25)
	genre = models.CharField(max_length=25,choices=CHOICES)
	playback = models.FileField(upload_to='media/')
	producer = models.ForeignKey('Producer',on_delete=models.CASCADE),

	def __str__(self):
		return self.name
