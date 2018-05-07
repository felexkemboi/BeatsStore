from django.db import models
from django import forms
from django.db.models import TextField
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField



# Create your models here
class Producer(models.Model):
	username = models.CharField(max_length=25)
	phone = models.IntegerField()
	email = models.EmailField()

	def __str__(self):
		return self.username




CHOICES=(
	        ('BONGO','Bongo'),
        	('GOSPEL', 'Gospel'),
        	('REGGAE', 'Reggae'),
        	('HIPHOP', 'Hiphop'),
        	('BLUES', 'Blues'),
        	('R & B', 'R & B'),
       		('ROCK', 'rock'),
			('SOUND TRACK', 'Sound_Track'),
    )

CHOICE=(
	        ('SHOOTING','Shooting'),
        	('RECORDING', 'Recording'),
        	('PHOTO-SHOOTING', 'Photo-Shooting'),
        	
    )
class Beat(models.Model):
	name = models.CharField(max_length=25)
	genre = models.CharField(max_length=25,choices=CHOICES)
	playback = models.FileField(upload_to='media/')
	producer = models.ForeignKey('Producer',on_delete = models.SET_NULL,null= True)
	#book  =    models.ForeignKey('Book', on_delete = models.SET_NULL,null= True)

	def __str__(self):
		return self.name

class Session(models.Model):
    from_date             = models.DateTimeField()
    to_date               = models.DateTimeField()
    service               = models.CharField(max_length=25,choices=CHOICE)
    phone                 = models.IntegerField()
    alternative_phone     = models.IntegerField()
    description           = models.CharField(max_length=255)

    
    """
    def __str__(self):
        return self.from_date"""

