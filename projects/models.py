from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse

from django.db.models.signals import pre_save
from django.dispatch import receiver

from mptt.models import TreeForeignKey, MPTTModel
from tinymce.models import HTMLField
import slugify
# Create your models here.


class ProjectManager(models.Manager):

    def active_for_site(self):
        return super(ProjectManager, self).filter(active=True)

    def first_page(self):
        return self.active_for_site().filter(first_page=True)[:4]


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(unique=True, max_length=100)
    image = models.ImageField(blank=True, null=True)
    active = models.BooleanField(default=False)
    first_page = models.BooleanField(default=False)
    demo = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)
    category = models.ManyToManyField(Category, blank=True, null=True)
    first_page_text = models.CharField(max_length=250, blank=True, null=True)
    text = HTMLField(blank=True, null=True)
    href = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    my_query = ProjectManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def tiny_image(self):
        return mark_safe('<img src="%s" style="width:100px; heightL100px;">'% self.image.url) if self.image else None
    tiny_image.description = 'Image'

    def get_absolute_url(self):
        return reverse('projects:view', kwargs={'slug':self.slug})


@receiver(pre_save, sender=Project)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        new_slug = slugify.slugify(instance.title)
        instance.slug = new_slug
        instance.save()