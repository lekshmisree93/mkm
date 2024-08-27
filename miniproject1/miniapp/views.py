from django.shortcuts import render
from.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gallary(request):
    return render(request, 'gallary.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def packages(request):
    return render(request,'packages.html')

def booking(request):
    bok=book.objects.all()
    return render(request,'booking.html',{'bok':bok})
