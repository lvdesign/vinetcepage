# Generated by Django 3.1.12 on 2022-01-18 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vins', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
        migrations.AddField(
            model_name='tag',
            name='description_tag',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description_cat',
            field=models.TextField(blank=True, null=True),
        ),
    ]
