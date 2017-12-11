# Generated by Django 2.0 on 2017-12-11 08:22

import blog.models
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_image, validators=[blog.models.validate_size])),
                ('active', models.BooleanField(default=False)),
                ('first_page', models.BooleanField(default=False)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('first_page_text', models.CharField(blank=True, max_length=250, null=True)),
                ('text', tinymce.models.HTMLField(blank=True, null=True)),
                ('github_url', models.URLField(blank=True, null=True)),
            ],
            managers=[
                ('my_query', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.CategoryBlog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='blog.CategoryBlog'),
        ),
    ]
