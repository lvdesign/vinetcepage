from django.contrib import admin


from vins.models import Vin, Comment, Category, Tag, Fav 
# Register your models here.


class CommentInline(admin.TabularInline): # new
    ''' commentaites ajouté à la suite de vin '''
    model = Comment
    extra = 0
   

class VinAdmin(admin.ModelAdmin):
    search_fields= ['title']
    fields = ('title', 'author','slug', 'decription', 'price', 'boutique', 'tips', 'image', 'category', 'tag','score')
    prepopulated_fields = {'slug': ('title', )}

    inlines = [
        CommentInline,
        ]

admin.site.register(Vin, VinAdmin)



admin.site.register(Comment)

admin.site.register(Category)

admin.site.register(Tag)

admin.site.register(Fav)