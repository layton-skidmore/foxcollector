from django.forms import ModelForm
from .models import Habitats

class HabitatsForm(ModelForm):
  class Meta:
    model = Habitats
    fields = ['date', 'habitat']