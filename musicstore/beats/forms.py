from django import forms
from django.contrib.auth.models import User
from . models import Beat,Producer,Session

class BeatForm(forms.ModelForm):
	class Meta:
		model = Beat
		fields = ('name','genre','playback')

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('from_date','to_date','service','phone','description','alternative_phone',)

        widgets = {
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
        }
