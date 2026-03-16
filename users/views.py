from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

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
      return redirect('register') 

    if len(senha) < 6:
      return redirect('register') 
    
    users = User.objects.filter(username=username)
    
    if users.exists():
      return redirect('register')

    User.objects.create_user(
      username = username,
      password = senha
    )
    
    return redirect('login')