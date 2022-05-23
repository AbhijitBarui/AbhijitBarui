from django.urls import path
from . import views

urlpatterns = [
    path('', views.routine, name='routine'),
    path('getroutine', views.getroutine, name='getroutine'),
    path('postroutine', views.postroutine, name='postroutine'),
]