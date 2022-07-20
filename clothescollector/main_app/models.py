from django.db import models
from django.urls import reverse

# Create your models here.
PARTS = (
    ('L', 'Length'),
    ('W', 'Width'),
    ('D', 'Design')
)

class Cloth(models.Model):
    brand = models.CharField(max_length=100)
    type_cloth = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.brand


    # class ClothCreate(CreateView):
    #     model = Cloth
    #     fields = '__all__'
    #     # success_url = '/clothes/'

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



    
