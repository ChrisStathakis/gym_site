from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass
