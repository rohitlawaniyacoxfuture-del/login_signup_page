from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('signup')

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):

    # 👇 Agar dashboard se redirect hua hai
    if request.GET.get('next'):
        messages.error(request, "You're not authenticated user. Please login.")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            # 👇 Login ke baad usi page par bheje jaha se aaya tha
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')

    return render(request, 'login.html')


@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')