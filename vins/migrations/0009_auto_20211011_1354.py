# Generated by Django 3.1.12 on 2021-10-11 13:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vins', '0008_auto_20211007_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='description_tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description_cat',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]