from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('list/', views.list, name='list'),
    #path('ipconfig/', views.ipconfig, name='ipconfig'),
    #path('cpu_usage/', views.cpu_usage, name='cpu_usage')
]