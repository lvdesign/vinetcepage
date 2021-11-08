# Generated by Django 3.1.12 on 2021-11-08 15:01

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('sud-ouest', 'Sud Ouest'), ('bordeaux', 'Bordeaux'), ('bourgogne', 'Bourgogne'), ('val-de-loire', 'Val De Loire'), ('languedoc-roussillon', 'Languedoc Roussillon'), ('vallée-du-rhône', 'Vallée Du Rhône'), ('savoie', 'Savoie'), ('corse', 'Corse'), ('beaujolais', 'Beaujolais'), ('alsace-lorraine', 'Alsace Lorraine'), ('provence', 'Provence'), ('centre-loire', 'Centre Loire'), ('jura', 'Jura')], default='bordeaux', max_length=40)),
                ('slug', models.SlugField(max_length=40, null=True, unique=True)),
                ('description_cat', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
                'unique_together': {('name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(validators=[django.core.validators.MinLengthValidator(1, 'Commentaire doit être plus grand que 1 caractère. '), django.core.validators.MaxLengthValidator(141, 'Le commentaire ne doit pas dépasser 140 caractères !')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_authors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favs_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('abouriou', 'Abouriou'), ('bourboulenc', 'Bourboulenc'), ('braucol', 'Braucol'), ('cabernet', 'Cabernet'), ('cabernet-Franc', 'Cabernet Franc'), ('cabernet-Sauvignon', 'Cabernet Sauvignon'), ('caladoc', 'Caladoc'), ('camaralet', 'Camaralet'), ('carignan', 'Carignan'), ('carignan-blanc', 'Carignan Blanc'), ('chardonnay', 'Chardonnay'), ('chenin', 'Chenin'), ('chenin-blanc', 'Chenin Blanc'), ('cinsault', 'Cinsault'), ('clairette', 'Clairette'), ('colombard', 'Colombard'), ('courbu', 'Courbu'), ('egiodola', 'Egiodola'), ('gamay', 'Gamay'), ('grenache', 'Grenache'), ('grenache-blanc', 'Grenache Blanc'), ('grenache-gris', 'Grenache Gris'), ('grenache-noir', 'Grenache Noir'), ('gros-Manseng', 'Gros Manseng'), ('loin-de-l-oeil', 'Loin De L Oeil'), ('macabeu', 'Macabeu'), ('malbec', 'Malbec'), ('marsanne', 'Marsanne'), ('marselan', 'Marselan'), ('mauzac', 'Mauzac'), ('melon-de-Bourgogne', 'Melon De Bourgogne'), ('merlot', 'Merlot'), ('mourvèdre', 'Mourvèdre'), ('muscadelle', 'Muscadelle'), ('muscat-petits-grains', 'Muscat Petits Grains'), ('negrette', 'Negrette'), ('petit-Courbu', 'Petit Courbu'), ('petit-Manseng', 'Petit Manseng'), ('petit-Verdot', 'Petit Verdot'), ('pineau-dAunis', 'Pineau D Aunis'), ('pinot-noir', 'Pinot Noir'), ('poulsard', 'Poulsard'), ('rolle', 'Rolle'), ('roussanne', 'Roussanne'), ('sauvignon', 'Sauvignon'), ('sauvignon-blanc', 'Sauvignon Blanc'), ('sauvignon-gris', 'Sauvignon Gris'), ('savagnin', 'Savagnin'), ('syrah', 'Syrah'), ('sémillon', 'Sémillon'), ('tannat', 'Tannat'), ('tressailler', 'Tressailler'), ('ugni-blanc', 'Ugni Blanc'), ('vermentino', 'Vermentino'), ('viognier', 'Viognier')], default='merlot', max_length=30)),
                ('slug', models.SlugField(max_length=30, null=True, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['name'],
                'unique_together': {('name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Vin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('title', models.CharField(max_length=250, unique=True, validators=[django.core.validators.MinLengthValidator(3, 'Le titre doit avoir plus de 3 caractères !')])),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('tips', models.CharField(max_length=141, validators=[django.core.validators.MaxLengthValidator(141, 'Le conseil ne doit pas dépasser 140 caractères !')])),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='PNG', keep_meta=True, null=True, quality=75, size=[300, 300], upload_to='vinslv/')),
                ('price', models.CharField(blank=True, choices=[('moins de 10', 'Moins De 10'), ('de 10 à 20', 'De 10 A 20'), ('plus de 20', 'Plus De 20')], default='de 10 à 20', max_length=11, null=True)),
                ('boutique', models.CharField(blank=True, max_length=141, null=True, validators=[django.core.validators.MaxLengthValidator(141, 'Boutique ne doit pas dépasser 140 caractères !')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fav_vin_auteur', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(help_text='Selectionnez une region pour ce vin.', on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='vins.category')),
                ('comments', models.ManyToManyField(related_name='vin_comment', through='vins.Comment', to=settings.AUTH_USER_MODEL)),
                ('favorites', models.ManyToManyField(related_name='favorite_vins', through='vins.Fav', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(help_text='Selectionnez des cépages pour ce vin.', related_name='tags', to='vins.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='fav',
            name='vin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vins.vin'),
        ),
        migrations.AddField(
            model_name='comment',
            name='vin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vins.vin'),
        ),
        migrations.AlterUniqueTogether(
            name='fav',
            unique_together={('vin', 'user')},
        ),
    ]
