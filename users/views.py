from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def register(request):
  if request.method == 'GET':
    return render(request, 'register.html')
  elif request.method == 'POST':
    print(request.POST)
    username = request.POST.get('username')
    senha = request.POST.get('senha')
    confirmar_senha = request.POST.get('confirmar_senha')
    
    if not senha == confirmar_senha:
      print('password is equal')
      messages.add_message(request, constants.ERROR, 'Senha e Confirmar Senha não são iguais.')
      return redirect('register') 

    if len(senha) < 6:
      print('password small')
      messages.add_message(request, constants.ERROR, 'Senha tem que ser maior do que 6 caracteres')
      return redirect('register') 
    
    users = User.objects.filter(username=username)
    
    if users.exists():
      print('user exist')
      messages.add_message(request, constants.ERROR, 'Usuário já existe')
      return redirect('register')

    User.objects.create_user(
      username = username,
      password = senha
    )
    
    return redirect('login')