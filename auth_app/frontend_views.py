from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
#from auth_app.forms import UserUpdateForm, ProfileUpdateForm
#from blog_app.models import Blog
from auth_app.models import User

# Create your views here.

def register(response):
    if response.method == 'POST':
        username = response.POST['username']
        email = response.POST['email']
        password = response.POST['password1']
        password2 = response.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(response, "This email already exists in our database")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(response, "This username already exists in our database")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #automatically login the new user
                user = auth.authenticate(username=username, password=password)
                auth.login(response, user)

                #instant profile creation for new user
                return redirect('register')

        else:
            messages.info(response, "The passwords do not match")
            return redirect('register')

    else:
        return render(response, 'auth_app/register.html')

def login(response):
    if response.method == 'POST':
        username = response.POST['username']
        password = response.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(response, user)
            return redirect('index')

        else:
            messages.info(response, "Invalid Credentials")
            return redirect('login')

    return render(response, 'auth_app/login.html')


def ProfilePage(response):
    user_posts = Blog.objects.all()
    return render(response, 'auth_app/profile.html', {'user_posts':user_posts})

def logout(response):
    auth.logout(response)
    return redirect('index')
