from django.urls import path,include
from . import views

urlpatterns = [
    path('',                    views.shop,             name='shop'),
    path('producers/',          views.allproducers,     name ='allproducers'),
    path('producers/<int:pk>/', views.producerbeats,    name ='producerbeats')
]



