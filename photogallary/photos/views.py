from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from .models import Photo
from .forms import PhotoForm, ContactForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

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
    return render(request, "upload_photo.html", context)

def add_like(request, id):
    try:
        photo = get_object_or_404(Photo, id=id)
        photo.likes += 1
        photo.save()
    except ObjectDoesNotExist:
        return Http404
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


def add_dislike(request, id):
    try:
        photo = get_object_or_404(Photo, id=id)
        photo.dislikes += 1
        photo.save()
    except ObjectDoesNotExist:
        return Http404
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def photo_list_sort(request):
    queryset = Photo.objects.order_by('-likes', 'dislikes')
    context = {
        "photos": queryset
    }
    return render(request,"photo_list_sort.html", context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            flag_contact_saved = True
            send_mail('Contact', 'Look at this', 'example@gmail.com', ['m.n.demianenko@gmail.com'],)
            form = ContactForm()
            # do something.
    else:
        form = ContactForm()
        flag_contact_saved = False
    context = {
        "flag_contact": flag_contact_saved,
        "form_contact": form
    }
    return render(request, "contact.html", context)

#Django send email (заполнение контакта и на почту отправляется уведомление.)