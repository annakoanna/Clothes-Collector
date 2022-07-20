from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('clothes/', views.clothes_index, name='index'),
    path('clothes/<int:cloth_id>/', views.clothes_detail, name='detail'),
    path('clothes/create/', views.ClothCreate.as_view(), name='clothes_create'),
    path('clothes/<int:pk>/update/', views.ClothUpdate.as_view(), name='clothes_update'),
    path('clothes/<int:pk>/delete/', views.ClothDelete.as_view(), name='clothes_delete'),
    path('clothes/<int:cloth_id>/add_alter/', views.add_alter, name='add_alter'),

]