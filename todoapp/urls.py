from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todoapp-index'),
    path('about/', views.about, name='todoapp-about')
]   
