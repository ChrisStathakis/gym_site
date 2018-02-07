from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver

from mptt.models import TreeForeignKey, MPTTModel
from tinymce.models import HTMLField
import slugify
# Create your models here.


def image_size(value):
    if value.file.size> 1024*1024*0.6:
        raise ValidationError('This file is bigger than 0.5 mb.')
    return value


def location():
    pass


class Trainer(models.Model):
    active = models.BooleanField(default=True)
    first_page = models.BooleanField(default=True)
    name = models.CharField(unique=True, max_length=150)
    role = models.CharField(max_length= 200, default='Trainer')
    short_description = HTMLField(blank=True, null=True)
    image = models.ImageField()
    description = models.CharField(blank=True, max_length=250, null=True, default='Add descriprion here')
    instagram_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


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


class GymPart(models.Model):
    title = models.CharField(max_length=50)
    url_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(unique=True, max_length=100)
    image = models.ImageField(blank=True, null=True, validators=[image_size, ])
    active = models.BooleanField(default=False)
    first_page = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)
    first_page_text = models.CharField(max_length=250, blank=True, null=True)
    text = HTMLField(blank=True, null=True)
    max_time = models.TimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    rounds = models.IntegerField(default=1)
    my_query = ProjectManager()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def tiny_image(self):
        return mark_safe('<img src="%s" style="width:100px; heightL100px;">'% self.image.url) if self.image else None
    tiny_image.description = 'Image'

    def get_absolute_url(self):
        return reverse('projects:view', kwargs={'slug':self.slug})


class ProjectItems(models.Model):
    CHOICES = (())
    title = models.ForeignKey(GymPart, on_delete=models.CASCADE)
    project_related = models.ForeignKey(Project, on_delete=models.CASCADE)
    reps = models.CharField(default='As Many you can', max_length=100)
    reps_type = models.CharField(max_length=1,
                                 choices=(('a', 'Επαναλήψεις'),
                                            ('b', 'Χρόνος')
                                           ), default='a'
                                 )
    weight = models.IntegerField(default=0)
    description = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title.title



@receiver(pre_save, sender=Project)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        new_slug = slugify.slugify(instance.title)
        instance.slug = new_slug
        instance.save()