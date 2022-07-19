from django.db import models

# Create your models here.

class Cloth(models.Model):
    brand = models.CharField(max_length=100)
    type_cloth = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()

def __str__(self):
    return self.brand



    

# clothes = [
#   Cloth('Prada', 'dress', 'red, silk dress', 1200),
#   Cloth('Palm Angels', 'T-shirt', 'cotton', 410),
#   Cloth('Gucci', 'coat', 'leather fur', 3000)
# ]