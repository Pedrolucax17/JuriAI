from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from .models import Cliente
from django.contrib.auth.decorators import login_required

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

def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  elif request.method == 'POST':
    username = request.POST.get('username')
    senha = request.POST.get('senha')
    
    user = authenticate(username=username, password=senha)

    if user is not None:
      auth.login(request, user)
      return redirect('clientes')
    else:
      messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
      return redirect('login')
    
@login_required    
def clientes(request):
  if request.method == 'GET':
    clientes = Cliente.objects.filter(user=request.user)
    return render(request, 'clientes.html', {'clientes': clientes})
  elif request.method == 'POST':
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    tipo = request.POST.get('tipo')
    status = request.POST.get('status') == 'on'
    
    Cliente.objects.create(
      nome=nome,
      email=email,
      tipo=tipo,
      status=status,
      user=request.user
    )
    
    messages.add_message(request, constants.SUCCESS, 'Cliente cadastrado com sucesso!')
    return redirect('clientes')