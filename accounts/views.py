from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash

from .models import User

# Create your views here.
def index(request):
    users = User.objects.order_by("-pk")
    context = {
        "users": users,
    }

    return render(request, "accounts/index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:index")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect("accounts:index")
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)
    else:
        return redirect("accounts:index")

def detail(request, pk):
    users = User.objects.get(pk=pk)

    context = {"users": users}

    return render(request, "accounts/detail.html", context)

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')