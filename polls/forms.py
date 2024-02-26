from django.forms import ModelForm
from .models import fff

class Fffform(ModelForm):
    class Meta:
        model = fff
        fields= '__all__'