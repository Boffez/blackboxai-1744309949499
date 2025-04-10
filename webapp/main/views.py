from django.shortcuts import render
from .models import Car

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def cars(request):
    cars = Car.objects.all().order_by('-created_at')
    context = {
        'cars': cars
    }

    return render(request, 'main/cars.html', context)

def about(request):
    return render(request, 'main/about.html')