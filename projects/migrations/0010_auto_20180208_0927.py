# Generated by Django 2.0 on 2018-02-08 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gympart',
            name='url_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='projectitems',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]