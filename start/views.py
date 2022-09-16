from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User,auth
from addpost.models import Room
#from django.contrib.auth import login, logout

def home(request):
	
	return render(request, "start/home.html")

#Register form and functions
def register(request):

	if request.method == "POST":

		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']

		#if password1 and password2 matches it futhers checks the username, email & after every criteria is met it redirects to login page. 
		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Taken!!')
				return redirect('start:register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Taken!!')
			else:
				user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)					
				user.save();
				messages.info(request,'User Created')
				return redirect('start:login') 
		else:
			messages.info(request,'Password did not match!!')
			return redirect('start:register')
		return redirect('/')

	return render(request, "start/register.html")

#Login Functions 
def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request,'invalid credintials')
			return redirect('start:login')
	else:
		return render(request,'start/login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')		
