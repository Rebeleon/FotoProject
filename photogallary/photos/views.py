from django.shortcuts import render
from .models import Photo
from .forms import PhotoForm

def photo_list(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset
    }
    return render(request,"photo.html", context)

def photo_upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            flag_img_saved = True
            form = PhotoForm()
            # do something.
    else:
        form = PhotoForm()
        flag_img_saved = False
    context = {
        "flag_img": flag_img_saved,
        "form_photo": form
    }
    return render (request, "upload_photo.html", context)

