from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import *
from gallery.models import *

from mptt.admin import DraggableMPTTAdmin

# Register your models here.


class GalleryProjectTabular(GenericTabularInline):
    model = Gallery


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['tiny_image']
    list_filter = ['active', 'first_page',]
    list_display = ['title', 'active', 'first_page',]
    inlines = [GalleryProjectTabular, ]
    search_fields = ['title',]
    fieldsets = (
        ('General', {
            'fields': ('title',
                       ('active', 'first_page',),
                       ('tiny_image', 'image'),
                       )
        }),
        ('URL and Text', {
            'fields': ('first_page_text',
                       'text', 'slug',
                       ),
        }),
    )


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    pass
