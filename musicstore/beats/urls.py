from django.urls import path,include
from . import views

urlpatterns = [
    path('',                    views.shop,             name ='shop'),
    path('producers/',          views.allproducers,     name ='allproducers'),
    path('allbeats/',           views.allbeats,         name ='allbeats'),
    path('producers/<int:pk>/', views.producerbeats,    name ='producerbeats'),
    path('addbeat/<int:pk>/',   views.addbeat,          name ='addbeat'),
    path('booksession/',        views.booksession,      name ='booksession'),
    path('upcomingsessions/',   views.upcomingsessions, name ='upcomingsessions'),
]



