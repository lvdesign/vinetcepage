from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator,MaxLengthValidator, MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User
from django.conf import settings
from django.template.defaultfilters import slugify

from django.db.models import Count
from django.utils import timezone

# texte editor pour Category et Tag description
from ckeditor.fields import RichTextField

from django_resized import ResizedImageField
# Create your models here.


class Category(models.Model):
    ''' Category : les regions de vin avec leur description. '''
    class CategoryChoice(models.TextChoices):
        Sud_Ouest = 'sud-ouest'
        Bordeaux ='bordeaux'
        Bourgogne= 'bourgogne'
        Val_de_loire= 'val-de-loire'
        Languedoc_roussillon='languedoc-roussillon' 
        Vallée_du_rhône= 'vallée-du-rhône'
        Savoie= 'savoie'
        Corse= 'corse'
        Beaujolais= 'beaujolais'
        Alsace_lorraine= 'alsace-lorraine'
        Provence= 'provence'
        Centre_loire= 'centre-loire'
        Jura= 'jura'
    
    name = models.CharField( 
        max_length=40,       
        choices=CategoryChoice.choices,
        default=CategoryChoice.Bordeaux
    )
    slug = models.SlugField(max_length=40, unique=True, null=True)

    # description categorie
    description_cat = models.TextField(blank=True, null=True)
    #description_cat = RichTextField(blank=True, null=True)
   

    def __str__(self):
        return self.name  
    
    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])
   
    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = ('name', 'slug')

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category,self).save(*args, **kwargs)  


class Tag(models.Model):
    ''' Tag : les cépages de vin avec leur description. '''

    class TagChoice(models.TextChoices):
        Abouriou ='abouriou'
        Bourboulenc='bourboulenc'
        Braucol='braucol'
        Cabernet='cabernet'
        Cabernet_Franc='cabernet-Franc'
        Cabernet_Sauvignon = 'cabernet-Sauvignon'    
        Caladoc='caladoc'
        Camaralet='camaralet'
        Carignan='carignan'
        Carignan_blanc='carignan-blanc'
        Chardonnay='chardonnay'
        Chenin='chenin'
        Chenin_blanc='chenin-blanc'
        Cinsault='cinsault'
        Clairette='clairette'
        Colombard='colombard'
        Courbu='courbu'
        Egiodola='egiodola'
        Gamay='gamay'
        Grenache='grenache'
        Grenache_blanc='grenache-blanc'
        Grenache_gris='grenache-gris'
        Grenache_noir='grenache-noir'
        Gros_Manseng='gros-Manseng'
        Loin_de_l_oeil= 'loin-de-l-oeil'
        Macabeu='macabeu'
        Malbec='malbec'
        Marsanne='marsanne'
        Marselan='marselan'
        Mauzac='mauzac'
        Melon_de_Bourgogne='melon-de-Bourgogne'
        Merlot='merlot'
        Mourvèdre='mourvèdre'
        Muscadelle='muscadelle'
        Muscat_petits_grains='muscat-petits-grains'
        Negrette='negrette'
        Petit_Courbu='petit-Courbu'
        Petit_Manseng='petit-Manseng'
        Petit_Verdot='petit-Verdot'
        Pineau_d_Aunis='pineau-dAunis'
        Pinot_noir='pinot-noir'
        Poulsard='poulsard'
        Rolle='rolle'
        Roussanne='roussanne'
        Sauvignon='sauvignon'
        Sauvignon_blanc='sauvignon-blanc'
        Sauvignon_gris='sauvignon-gris'
        Savagnin='savagnin'
        Syrah='syrah'
        Sémillon='sémillon'
        Tannat='tannat'
        Tressailler='tressailler'
        Ugni_blanc='ugni-blanc'
        Vermentino='vermentino'
        Viognier='viognier'

    name = models.CharField(
        max_length=30,
        choices=TagChoice.choices,
        default=TagChoice.Merlot       
    )
    slug = models.SlugField(max_length=30, unique=True, null=True)
    description_tag = models.TextField(blank=True, null=True)
    #description = RichTextField(blank=True, null=True)

    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        unique_together = ('name', 'slug')

    def display_tag(self):
        return  ', '.join(tag.name for tag in self.tag.all()[:5])

    display_tag.short_description = 'Tag'

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Tag,self).save(*args, **kwargs)     






class Vin (models.Model):
    ''' Vin  model lié à Categorie pour la region et Tag pour le cépage'''
    tag = models.ManyToManyField( Tag,  help_text='Selectionnez des cépages pour ce vin.',  related_name='tags')
    category = models.ForeignKey(to=Category, help_text='Selectionnez une region pour ce vin.', on_delete=models.CASCADE, related_name='categories')
    
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Fav', related_name='favorite_vins')

    comments = models.ManyToManyField(settings.AUTH_USER_MODEL,  related_name='vin_comment', through='Comment') #NEW as Fav
 
    #rating
    score = models.IntegerField(default = 0,
    validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ]) #0 hasn't be rated yet

    title = models.CharField(max_length=250, validators=[MinLengthValidator( 3, "Le titre doit avoir plus de 3 caractères !")], unique=True)
    slug = models.SlugField(max_length=255,null=False, unique=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fav_vin_auteur')
    description = models.TextField()
    tips = models.CharField( max_length=141, validators=[MaxLengthValidator(141, "Le conseil ne doit pas dépasser 140 caractères !")] )

    #image = models.ImageField(upload_to='vinslv/', null=True, blank=True)
    # https://github.com/un1t/django-resized avec cloudinary media/vinslv/
    image = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to='vinslv/', null=True, blank=True)

    class PriceChoice(models.TextChoices):
        MOINS_DE_10 = 'moins de 10'
        DE_10_A_20 = 'de 10 à 20'
        PLUS_DE_20 ='plus de 20'

    price = models.CharField(
        max_length=11,
        choices=PriceChoice.choices,
        default=PriceChoice.DE_10_A_20,
        null=True, blank=True
    )


    boutique = models.CharField( max_length=141, validators=[MaxLengthValidator(141, "Boutique ne doit pas dépasser 140 caractères !")] , null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return reverse('vins:vin_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Vin,self).save(*args, **kwargs)


# Comment class
class Comment(models.Model) :
    text = models.TextField(
        validators=[MinLengthValidator(1, "Commentaire doit être plus grand que 1 caractère. "), MaxLengthValidator(141, "Le commentaire ne doit pas dépasser 140 caractères !")]
    )

    vin = models.ForeignKey(Vin, on_delete=models.CASCADE )# related_name='comments'
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments_authors") #NEW

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15 : return self.text
        return self.text[:11] + ' ...'

    #def get_absolute_url(self):
        #return reverse('vin_detail')      


# FAV
class Fav(models.Model) :
    ''' Vin Favoris pour chaque Membre'''
    vin = models.ForeignKey( Vin, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='favs_users')

    # https://docs.djangoproject.com/en/3.0/ref/models/options/#unique-together
    class Meta:
        unique_together = ('vin', 'user')

    def __str__(self) :
        return '%s likes %s'%(self.user.username, self.vin.title[:10])
