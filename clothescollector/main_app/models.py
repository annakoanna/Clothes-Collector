from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
PARTS = (
    ('L', 'Length'),
    ('W', 'Width'),
    ('D', 'Design')
)

class Accessory(models.Model):
  name = models.CharField(max_length=50)
  size = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})


class Cloth(models.Model):
    brand = models.CharField(max_length=100)
    type_cloth = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    accessories = models.ManyToManyField(Accessory)

    def __str__(self):
        return self.brand
        
 
    def fed_for_today(self):
        return self.alter_set.filter(date=date.today()).count() >= len(PARTS)  


    def get_absolute_url(self):
        return reverse('detail', kwargs={'cloth_id': self.id})

class Alter(models.Model):
  date = models.DateField('altering date')
  part = models.CharField(max_length=1, choices=PARTS, default=PARTS[0][0])

  cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_part_display()} on {self.date}"

  class Meta:
    ordering = ['-date']



    
