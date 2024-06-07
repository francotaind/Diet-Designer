from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meals/', include('meals.urls')),                                                
    path('accounts/', include('django.contrib.auth.urls')),                               
    path('accounts/', include('accounts.urls')),                                          
    path('counter/', include('counter.urls')),                                            
    path('recipe/', include('recipe.urls')),                                              
    path('store/', include('store.urls')),  
        ]
