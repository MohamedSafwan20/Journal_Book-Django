from django.contrib.auth import login, logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('user:login')
