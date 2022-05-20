
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  


def home(request):
    return render(request, 'index.html')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('/')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'register.html', {'form_usuario': form_usuario})