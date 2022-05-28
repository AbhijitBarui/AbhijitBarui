from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="urlshort"),
    path('create', views.create, name='create'),
    path('<str:slug>',views.real, name='real'),
]