from django import forms
from django.contrib.auth.models import User
from . models import Beat,Producer

class BeatForm(forms.ModelForm):
	class Meta:
		model = Beat
		fields = ('name','genre','playback')