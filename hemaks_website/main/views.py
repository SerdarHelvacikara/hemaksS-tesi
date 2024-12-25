from django.shortcuts import render
from .models import Machine

def home(request):
    machines = Machine.objects.all()  # Veritabanındaki tüm makineleri al
    return render(request, 'home.html', {'machines': machines})

# Create your views here.
def products(request):
    machines = Machine.objects.all()  # Tüm makineleri alıyoruz
    return render(request, 'products.html', {'machines': machines})

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')