from django.forms import ModelForm
from .models import Alter

class AlterForm(ModelForm):
  class Meta:
    model = Alter
    fields = ['date', 'part']