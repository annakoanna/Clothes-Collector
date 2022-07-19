from django.shortcuts import render
from .models import Cloth

# Create your views here.
from django.http import HttpResponse




def home(request):
    return HttpResponse('<h1>Hello !!!</h1>')

def about(request):
    return render(request, 'about.html')

def clothes_index(request):
    clothes = Cloth.objects.all()
    return render(request, 'clothes/index.html', {'clothes': clothes })

def clothes_detail(request, cloth_id):
    cloth = Cloth.objects.get(id=cloth_id)
    return render(request, 'clothes/detail.html', { 'cloth': cloth })