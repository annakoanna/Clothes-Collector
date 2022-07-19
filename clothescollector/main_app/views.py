from django.shortcuts import render
from .models import Cloth
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

class ClothCreate(CreateView):
  model = Cloth
  fields = '__all__'

class ClothUpdate(UpdateView):
  model = Cloth
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['type_cloth', 'description', 'price']

class ClothDelete(DeleteView):
  model = Cloth
  success_url = '/clothes/'
