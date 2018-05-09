from django.shortcuts import render,get_object_or_404,redirect,render
from . models import Beat,Producer,Session
from .forms import BeatForm
from .forms import SessionForm


# Create your views here.
def home(request):
	return render(request,'index.html')

def shop(request):
	beats = Beat.objects.all()
	producers = Producer.objects.all() #order_by('created_date')
	#return render(request,'home.html', {'posts': posts,'ebooks':ebook,})
	return render(request,'test.html',{'beats': beats,'producers':producers})

def producerbeats(request,pk):
	producer = get_object_or_404(Producer,pk=pk)
	beats = Beat.objects.filter(producer = producer)
	return render(request,'producerbeats.html',{'beats': beats})

def allproducers(request):
	producers = Producer.objects.all()
	return render(request,'allproducers.html',{'producers':producers})

def allbeats(request):
	beats = Beat.objects.all()
	return render(request,'allbeats.html',{'beats': beats})

def addbeat(request,pk):
    if request.method == 'POST':
        form = BeatForm(request.POST,request.FILES)
        if form.is_valid():
            beat = form.save(commit=False)
            #topic.board = board
            producer = get_object_or_404(Producer,pk=pk)
            #form.save()
            beat = Beat.objects.create(
                name=form.cleaned_data.get('name'),
                genre=form.cleaned_data.get('genre'),
                playback=form.cleaned_data.get('playback'),
                producer = producer
            )
            beat.save()
            return redirect('allbeats')  # TODO: redirect to the created topic page
    else:
        form = BeatForm()
    return render(request, 'addbeat.html', {'form': form})

def booksession(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
        	#user = get_object_or_404(Producer,pk=pk)
            session = form.save(commit=False)
            session = Session.objects.create(
               from_date =form.cleaned_data.get('from_date'),
               to_date   =form.cleaned_data.get('to_date'),
                service  =form.cleaned_data.get('service'),
                phone    =form.cleaned_data.get('phone'),
                alternative_phone = form.cleaned_data.get('alternative_phone'),
                #user      =user,
                description = form.cleaned_data.get('description'),
            )
            #request.session['pk']=booking.pk
            session.save()
            return redirect('upcomingsessions')  # TODO: redirect to the created topic page
    else:
        form = SessionForm()
    return render(request, 'booksession.html', {'form': form})

def upcomingsessions(request):
	sessions = Session.objects.all()
	return render(request,'upcomingsessions.html',{'sessions':sessions})



	

