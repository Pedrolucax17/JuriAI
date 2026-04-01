from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('clientes/', views.clientes, name='clientes'),
  path("cliente/<int:id>", views.cliente, name='cliente'),
]