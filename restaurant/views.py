# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
<<<<<<< HEAD
#from .models import Menu
from .models import Menu


=======
from .models import Menu



>>>>>>> 49ddca9892d8ce8080d3c1e09a4d79bda59804d4
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

<<<<<<< HEAD
# Add your code here to create new views
def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu})
=======
# Add your code here to create new views
>>>>>>> 49ddca9892d8ce8080d3c1e09a4d79bda59804d4
