from django.shortcuts import render, redirect
from .models import Cloth
from .forms import AlterForm
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
    alter_form = AlterForm()
    return render(request, 'clothes/detail.html', { 'cloth': cloth, 'alter_form': alter_form })

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
  
