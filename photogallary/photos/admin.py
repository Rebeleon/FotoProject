from django.contrib import admin
from .models import Photo, Contact

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp"]

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Contact, ContactAdmin)