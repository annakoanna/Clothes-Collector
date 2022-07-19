from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('clothes/', views.clothes_index, name='index'),
    path('clothes/<int:cloth_id>/', views.clothes_detail, name='detail'),

]