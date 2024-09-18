from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('obra/<str:set_id>/', views.obra, name='obra'),
]