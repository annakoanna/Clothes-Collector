from django.shortcuts import render, redirect
from .models import Cloth, Accessory
from .forms import AlterForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
# from django.http import HttpResponse


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def clothes_index(request):
  clothes = Cloth.objects.all()
  return render(request, 'clothes/index.html', {'clothes': clothes })

def clothes_detail(request, cloth_id):
  cloth = Cloth.objects.get(id=cloth_id)
  id_list = cloth.accessories.all().values_list('id')
  accessories_cloth_doesnt_have = Accessory.objects.exclude(id__in=id_list)
  
  alter_form = AlterForm()
  return render(request, 'clothes/detail.html', { 'cloth': cloth, 'alter_form': alter_form, 'accessories': accessories_cloth_doesnt_have })


   

class ClothCreate(CreateView):
  model = Cloth
  fields = ['brand', 'type_cloth', 'description', 'price']

class ClothUpdate(UpdateView):
  model = Cloth
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['type_cloth', 'description', 'price']

class ClothDelete(DeleteView):
  model = Cloth
  success_url = '/clothes/'

def add_alter(request, cloth_id):
  form = AlterForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_alter = form.save(commit=False)
    new_alter.cloth_id = cloth_id
    new_alter.save()
  return redirect('detail', cloth_id=cloth_id)


class AccessoryList(ListView):
  model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'size']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'

def assoc_accessory(request, cloth_id, accessory_id):
  # Note that you can pass a toy's id instead of the whole toy object
  Cloth.objects.get(id=cloth_id).accessories.add(accessory_id)
  return redirect('detail', cloth_id=cloth_id)
  
