from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import *
from gallery.models import *

from mptt.admin import DraggableMPTTAdmin

# Register your models here.


class GalleryProjectTabular(GenericTabularInline):
    model = Gallery


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['tiny_image']
    list_filter = ['active', 'first_page', 'category']
    list_display = ['title', 'active', 'first_page', ]
    inlines = [GalleryProjectTabular, ]
    search_fields = ['title',]
    fieldsets = (
        ('General', {
            'fields': ('title',
                       ('active', 'first_page'),
                       ('tiny_image', 'image', 'category'),
                       )
        }),
        ('URL and Text', {
            'fields': ('first_page_text',
                       'text',
                       ('github_url'),
                       'slug',
                       ),
        }),
    )


@admin.register(CategoryBlog)
class CategoryBlogAdmin(DraggableMPTTAdmin):
    pass

