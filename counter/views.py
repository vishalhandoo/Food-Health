
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SignUpForm
from .models import UserProfile
from django.template import RequestContext
from .utils import calculate_bmi, calculate_daily_calories
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    import json
    import requests
    
    # Your existing code for processing POST requests and fetching API data
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
            api_request = requests.get(
                api_url + query, headers={'X-Api-Key': 'yZv8BJQwzNLMwpJZDmRXaA==WCavnBCvYAklYGL3'})
            try:
                api = json.loads(api_request.content)
                print(api_request.content)
            except Exception as e:
                api = "oops! There was an error"
                print(e)
            return render(request, 'home.html', {'api': api, 'query': query})
        else:
            return render(request, 'home.html', {'query': 'Enter a valid query'})
    else:
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                height = user_profile.height
                weight = user_profile.weight
                username=request.user.username
                bmi = calculate_bmi(height, weight)
                if user_profile.gender == 'male':  
                    bmr = 10 * weight + 6.25 * height * 100 - 5 * user_profile.age + 5
                else:
                    bmr = 10 * weight + 6.25 * height * 100 - 5 * user_profile.age - 161

                daily_calories = calculate_daily_calories(bmi) 
            except UserProfile.DoesNotExist:
                pass  

        return render(request, 'home.html', {'bmi': bmi, 'username': username, 'daily_calories': daily_calories})
    
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            UserProfile.objects.create(user=user, height=height, weight=weight)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
    
