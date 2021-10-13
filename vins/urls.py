# articles/urls.py
from django.urls import path, reverse_lazy, reverse

from . import views

"""
from vins.views import (
    VinListView, 
    VinUpdateView, 
    VinDetailView, 
    VinDeleteView, 
    VinCreateView,
    rate_image,
    AddFavoriteView,
    DeleteFavoriteView,
    CategoryDetailView,
    TagListView,
    TagDetailView,
)
"""

app_name= 'vins'

urlpatterns = [
    path('new/', views.VinCreateView.as_view(success_url=reverse_lazy('vins:vin_list')), name='vin_new'), # new
    path('<slug:slug>/edit/',views.VinUpdateView.as_view( success_url=reverse_lazy('vins:vin_list')), name='vin_edit'),     
    path('<slug:slug>/delete/',views.VinDeleteView.as_view(success_url=reverse_lazy('vins:vin_list')), name='vin_delete'), # new

    path('<slug:slug>/',views.VinDetailView.as_view(), name='vin_detail'), 
    path('', views.VinListView.as_view(), name='vin_list'),

    #path('rate/', rate_image, name='rate-view'),
]

urlpatterns +=[     
    path('category/', views.CategoryListView.as_view(), name='category_list'),  
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),    
]

urlpatterns +=[ 
    path('tag/', views.TagListView.as_view(), name='tag_list'), 
    path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag_detail'),    
]

urlpatterns +=[ 
    path('<int:pk>/favorite', views.AddFavoriteView.as_view(), name='vin_favorite'),
    path('<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='vin_unfavorite'),
]



