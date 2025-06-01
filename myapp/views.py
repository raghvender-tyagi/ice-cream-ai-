from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate  # Django ka built-in authentication system
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.contrib.auth  import login, logout

from django.shortcuts import render, redirect
from .models import IceCream
from.models import User
import sys
import os

# 'model' folder ka absolute path add karo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'model')))

# Ab import karo
from llama import get_bot_response    
 
def home(request):
    if request.method == 'POST':
      
        name = request.POST.get('name')  
        flavor = request.POST.get('flavor')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

       
        IceCream.objects.create(
            name=name,
            flavor=flavor,
            price=price,
            stock=stock
        )

        
        return redirect('home')
    
    return render(request, 'myapp/home.html')  


def learndynamic(request):
    # Dynamic data
    print("Inside learndynamic view")  # Add this line
    items = ['chl', 're', 'bidu', 'ekdum hero mafik']

    # Render the HTML template and pass the dynamic data to it
    return render(request, 'myapp/learndynamic.html', {'items': items})


def About(request):
    return render(request,'myapp/about.html')

def Login(request):





    
  if request.method == "POST":
        # Fetch values from the form
        username= request.POST.get('username')
        password= request.POST.get('password1')
        if User.objects.filter(username=username).exists():
            return HttpResponse("This username is already taken. Please try a different one.")

        if not username:
            return HttpResponse("Username or Password missing!")
        if not password:
            return HttpResponse(" Password missing")

        User.objects.create( 
            username=username,
            password=password
        )
        # Process the fetched values (for now, just return them in the response)
        # return HttpResponse(f"Username: {username}, Password: {password}")

       # Render the login page for GET request
  return render(request, 'myapp/login.html')

def signup(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)

            
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     if User.objects.filter(username=username).exists():
    #         return HttpResponse("This username is already taken. Please try a different one.")

    #     User.objects.create(
    #         username=username,
    #         password=password
    #     )
    #     return redirect('signup')
    # return render(request, 'myapp/signup.html')   
    pass
def dashboard_view(request):
    pass
def AI(request):
    if request.method == "POST":
        user_message = request.POST.get("user_input")
        print(user_message)
        bot_response=get_bot_response(user_message)
        print(bot_response)
        # Yahan tum apne AI model ko call kar sakte ho 👇
        # bot_response = f" {user_message}"  # Ye bas demo response hai
        
        return render(request, "myapp/AI.html", {"user_message": user_message, "bot_response": bot_response})
    
    return render(request, "myapp/AI.html")