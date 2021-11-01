from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .form import ProfileForm, CustomUserCreationForm
from .models import Profile

def profile(request, username=None):

    user_profile = None

    if username == None:
        if request.user.is_authenticated:
            user_profile = Profile.objects.get(user__username=request.user.username)
        else:
            return redirect('login')
    else:
        user_profile = Profile.objects.get(user__username=username)
    
    context = {
        'user_profile': user_profile
    }
    return render(request, "users/profile.html", context)


def logIn(request):
    form_type = "login"

    if request.user.is_authenticated:
        return redirect("profile-own")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Wrong username or password!")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile-own")

    context = {"form_type": form_type}

    return render(request, "users/login_register.html", context)


def logOut(request):
    logout(request)
    messages.success(request, 'Logout successful. Login again')
    return redirect('login')


def register(request):

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.username = user.username.lower()

            profile = profile_form.save(commit=False)
            profile.user = user

            user.save()
            profile.save()

            messages.success(request, "User account created!")
            login(request, user)
            return redirect('profile-own')
        else:
            message.error(request, 'Error creating user')
    else:
        profile_form = ProfileForm()
        user_form = CustomUserCreationForm()
    form_type = "register"

    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'form_type': form_type
    }

    return render(request, 'users/login_register.html', context)
    
