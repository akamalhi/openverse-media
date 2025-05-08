from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ..models import CustomUser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def handle_register(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('home')

        username = email  # use email as username
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=full_name
        )
        messages.success(
            request, "Registration successful. You can now log in.")
        return redirect('home')

    return redirect('home')

@csrf_exempt
def handle_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        username = email  # email used as username
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('home')

    return redirect('home')


def handle_logout(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect('home')

@csrf_exempt
def handle_profile(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = request.user
        user.first_name = full_name
        user.email = email
        if password:
            user.set_password(password)
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect('home')

    return redirect('home')