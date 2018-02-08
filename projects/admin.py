from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import *
from gallery.models import *

from mptt.admin import DraggableMPTTAdmin

# Register your models here.


class ProjectItemTabular(admin.TabularInline):
    model = ProjectItems
    extra = 3
    exclude = ['description']


class GalleryProjectTabular(GenericTabularInline):
    model = Gallery


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    pass


@admin.register(GymPart)
class GymPartAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectItems)
class ProjectItemsAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ['tiny_image']
    list_filter = ['active', 'first_page', 'category', ]
    list_display = ['title', 'active', 'first_page',]
    inlines = [ProjectItemTabular, GalleryProjectTabular, ]
    search_fields = ['title',]
    fieldsets = (
        ('General', {
            'fields': ('title',
                       ('active', 'first_page', 'category'),
                       ('rounds', 'max_time'),
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
