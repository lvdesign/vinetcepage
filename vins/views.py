from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # new
from django.views import View

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from vins.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from django.urls import reverse_lazy
from .models import Vin, Fav, Category, Tag
from django.http import JsonResponse

from django.shortcuts import render, redirect, get_object_or_404 #mail
from vins.utils import dump_queries





# VIN
class VinListView(OwnerListView):
    ''' Vins : liste, visible par tous'''
    model = Vin
    template_name = 'vin_list.html'

    def get(self,request):
        vin_list = Vin.objects.all()
        print(vin_list)

        favorites = list()
        if request.user.is_authenticated:
            rows = request.user.favorite_vins.values('id')
            favorites= [ row['id'] for row in rows]
        print(favorites)
        ctx = {'vin_list': vin_list, 'favorites': favorites}
        #dump_queries()
        retval = render(request, self.template_name, ctx)
        return retval

class VinDetailView(OwnerDetailView): # new
    ''' Vins : detail visible par tous'''
    model = Vin
    template_name = 'vin_detail.html'

def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val =request.POST.get('val')
        obj = Vin.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})

# CRUD
'''
CRUD section des vins
LoginRequiredMixin pour Creta, Update, Delete
UserPassesTestMixin pour limiter user to Update et Delete

'''
class VinCreateView( OwnerCreateView): 
    ''' Creer/editer vins: 
    'title','slug','decription','price','boutique','tips','image','category','tag','score' '''    
    model = Vin
    template_name = 'vin_new.html'   
    fields = 'title','slug','decription','price','boutique','tips','image','category','tag','score' #'__all__'   

    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

class VinUpdateView(OwnerUpdateView): # new
    ''' Update vins '''
    model = Vin
    fields = 'title','slug','decription','price','boutique','tips','image','category','tag','score'
    template_name = 'vin_edit.html'

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class VinDeleteView(DeleteView): # new
    ''' Delete vins '''
    model = Vin
    template_name = 'vin_delete.html'
    success_url = reverse_lazy('vin_list')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user





# Category -> region
class CategoryListView(OwnerListView):
    ''' Category/Region liste '''
    model = Category
    context_object_name = 'category_list'
    template_name = "category_list.html"

    def get_queryset(self):
        context_data = Category.objects.all()
        return context_data


class CategoryDetailView(OwnerDetailView):
    ''' Category/Region details '''
    model = Category
    template_name = "category_detail.html"

    def get_context_data(self, **kwargs):

        toto = Category.objects.all()
        #titi = Category.objects.filter('category').values()
        titi = Category.objects.filter().values('name')

        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['image'] = toto
        context['test'] = titi
        return context

    def get_queryset(self):
        return Category.objects.all()



# Tag -> Cepages
class TagListView(OwnerListView):
    ''' Tag/Cepage liste '''
    model = Tag
    context_object_name = 'tag_list'
    template_name = "tag_list.html"

    def get_queryset(self):
        return Tag.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagsall'] = Tag.objects.all()

        return context


class TagDetailView(OwnerDetailView):
    ''' Tag/Cepage detail '''
    model = Tag
    template_name = "tag_detail.html"

    def get_queryset(self):
        return Tag.objects.all()



# FAVORITE
''' Favoris Vin / User '''
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Vin PK",pk)
        t = get_object_or_404(Vin, id=pk)
        fav = Fav(user=request.user, vin=t)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        t = get_object_or_404(Vin, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, vin=t).delete()
        except Fav.DoesNotExist as e:
            pass

        return HttpResponse()


