from django.shortcuts import render,get_object_or_404,redirect,render
from . models import Beat,Producer
from .forms import BeatForm

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

def allbeats(request):
	beats = Beat.objects.all()
	return render(request,'allbeats.html',{'beats': beats})

def addbeat(request):
    #board = get_object_or_404(Board, pk=pk)
    #user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = BeatForm(request.POST)
        if form.is_valid():
            beat = form.save(commit=False)
            #topic.board = board
            user = request.user
            #form.save()
            beat = Beat.objects.create(
                name=form.cleaned_data.get('name'),
                genre=form.cleaned_data.get('genre'),
                playback=form.cleaned_data.get('playback'),
                producer = user
            )
            return redirect('allbeats')  # TODO: redirect to the created topic page
    else:
        form = BeatForm()
    return render(request, 'addbeat.html', {'form': form})


	

