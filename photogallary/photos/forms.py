from django.forms import ModelForm
from .models import Photo

# Create the form class.
class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']
