from django.shortcuts import render
from . models import Beat,Producer

# Create your views here.
def home(request):
	return render(request,'index.html')

def shop(request):
	beats = Beat.objects.all()
	producers = Producer.objects.all() #order_by('created_date')
	#return render(request,'home.html', {'posts': posts,'ebooks':ebook,})
	return render(request,'home.html',{'beats': beats,'producers':producers})

