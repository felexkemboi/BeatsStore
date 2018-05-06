from django.shortcuts import render,get_object_or_404,redirect,render
from . models import Beat,Producer

# Create your views here.
def home(request):
	return render(request,'index.html')

def shop(request):
	beats = Beat.objects.all()
	producers = Producer.objects.all() #order_by('created_date')
	#return render(request,'home.html', {'posts': posts,'ebooks':ebook,})
	return render(request,'home.html',{'beats': beats,'producers':producers})

def producerbeats(request,pk):
	producer = get_object_or_404(Producer,pk=pk)
	beats = Beat.objects.filter(producer = producer)
	return render(request,'producerbeats.html',{'beats': beats})

def allproducers(request):
	producers = Producer.objects.all()
	return render(request,'allproducers.html',{'producers':producers})

	

