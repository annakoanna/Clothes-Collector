from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Cloth:  # Note that parens are optional if not inheriting from another class
  def __init__(self, brand, type_cloth, description, price):
    self.brand = brand
    self.type_cloth = type_cloth
    self.description = description
    self.price = price

clothes = [
  Cloth('Prada', 'dress', 'red, silk dress', 1200),
  Cloth('Palm Angels', 'T-shirt', 'cotton', 410),
  Cloth('Gucci', 'coat', 'leather fur', 3000)
]



def home(request):
    return HttpResponse('<h1>Hello !!!</h1>')

def about(request):
    return render(request, 'about.html')

def clothes_index(request):
    return render(request, 'clothes/index.html', {'clothes': clothes })