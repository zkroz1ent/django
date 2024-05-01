
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

# This view will be for user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to a 'home' or 'index' view
        else:
            # Return an 'invalid login' error message.
            # TODO: Handle login errors and message display to the user.
            pass
    return render(request, 'login.html')

# This view will be for user signup
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirect to a 'home' or 'index' view
        else:
            # TODO: Handle signup errors and form display to the user.
            pass
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Application of login_required decorator to protect a view
@login_required
def protected_view(request):
    # This view requires a user to be logged in.
    return render(request, 'protected_view.html')

# URLs configuration
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    # TODO: Add other URL configurations here.
]

# Include a view for logout
def user_logout(request):
    logout(request)
    return redirect('login')
