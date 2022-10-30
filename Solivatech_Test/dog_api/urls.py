from django.urls import path

from . import views

urlpatterns = [

    path('index/', views.index, name='index'),
    path('dogs/', views.DogList.as_view(), name='dogs'),

    path('dogs/<int:id>', views.DogDetails.as_view(), name='dogs'),

    path('breeds/', views.BreedList.as_view(), name='breeds'),

    path('breeds/<int:id>', views.BreedDetails.as_view(), name='breeds'),


]