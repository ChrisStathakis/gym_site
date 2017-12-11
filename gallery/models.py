from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



def upload_location(instance, filename):
    return 'gallery/%s/%s' % (instance.id, filename)


def validate_size(value):
    if value.file.size > 0.5*1024*1024:
        raise ValidationError('This file is bigger than 0.5mb')


class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, validators=[validate_size, ])
    thumbnail = models.ImageField(validators=[validate_size, ], blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else 'Image %s' % self.id
