# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
#from .models import Menu
from .models import Product


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

# Add your code here to create new views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})