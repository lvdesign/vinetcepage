# pages/views.py
from django.views.generic import TemplateView

from vins.models import Vin, Tag, Category 

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self,**kwargs):

        context = super().get_context_data(**kwargs)

        context['vins'] = Vin.objects.all()
        
        # context['num_tag']= Tag.objects.all().count()

        # context['num_Category']= Category.objects.all().count()       


        context['me']= 'Hello'

        context['images'] = Vin.objects.all()
       

        return context





