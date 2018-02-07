# Generated by Django 2.0 on 2018-02-06 07:52

from django.db import migrations, models
import django.db.models.deletion
import projects.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20171231_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.CharField(default='As Many you can', max_length=100)),
                ('weight', models.IntegerField(default=0)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='max_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='rounds',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', validators=[projects.models.image_size]),
        ),
        migrations.AddField(
            model_name='projectitems',
            name='project_related',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AddField(
            model_name='projectitems',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.GymPart'),
        ),
    ]