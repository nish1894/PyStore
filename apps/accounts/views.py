from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("POST DATA:", request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            print("User created successfully" + user.email)
            login(request, user)
            messages.success(request, "Registration successful!")

            return redirect('register')
        else:
            print("Form is not valid")
            print(form.errors)
            # return 'home'
            return render(request, 'accounts/register.html', {'form': form})

    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})




def signin(request):
    def signin(request):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect if already logged in
        # Rest of the code remains the same
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to the home page after login
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'accounts/login.html', {'email': email})  # Keep the email pre-filled
    return render(request, 'accounts/login.html')

def home(request):
    # return HttpResponse("This is register page")
    return render(request,"accounts/home.html",{})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  # Redirect to the login page