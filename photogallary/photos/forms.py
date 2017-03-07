from django.forms import ModelForm
from .models import Photo, Contact

# Create the form class.
class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
