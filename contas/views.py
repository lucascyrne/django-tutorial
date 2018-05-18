from django.shortcuts import render, redirect, HttpResponse
from contas.forms import (
    RegistrationForm,
    EditPerfilForm,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'contas/home.html')

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = RegistrationForm()

    args = {'form':form}
    return render(request, 'contas/reg_form.html', args)

def view_perfil(request):
    args = {'user': request.user}
    return render(request, 'contas/perfil.html', args)

def edit_perfil(request):
    if request.method=='POST':
        form = EditPerfilForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('home:perfil'))
    else:
        form = EditPerfilForm(instance=request.user)
        args = {'form':form}
        return render(request, 'contas/edit_perfil.html', args)

def trocar_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('home:perfil'))
        else:
            return redirect(reverse('home:trocar_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'contas/trocar_password.html', args)
