from django.contrib import admin


from vins.models import Vin, Category, Tag, Fav 
# Register your models here.


class VinAdmin(admin.ModelAdmin):
    search_fields= ['title']
    fields = ('title', 'author','slug', 'decription', 'price', 'boutique', 'tips', 'image', 'category', 'tag','score')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Vin, VinAdmin)


admin.site.register(Category)

admin.site.register(Tag)

admin.site.register(Fav)