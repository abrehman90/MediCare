from django.shortcuts import render, redirect
from authy.forms import SignupForm
from django.contrib.auth.models import User
from authy.models import Profile
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.


def SideNavInfo(request):
	user = request.user
	nav_profile = None

	if user.is_authenticated:
		nav_profile = Profile.objects.get(user=user)

	return {'nav_profile': nav_profile}


def Signup(request):
	if request.method == 'POST' and 'action' in request.POST:
		form = SignupForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			print(username)
			email = form.cleaned_data.get('email')
			print(email)
			password = form.cleaned_data.get('password')
			User.objects.create_user(username=username, email=email, password=password)
			messages.info(request,"Your account has been successfully Registered, Now you LogIn ")
			return redirect('login')
	else:
		form = SignupForm()
		if request.user.is_authenticated:
			return redirect('index')
		else:
			if request.method == 'POST' and 'Signin' in request.POST:
				username = request.POST['username']
				print(username)
				password = request.POST['password']
				user = auth.authenticate(username=username, password=password)
				if user is not None:
					auth.login(request, user)
					return redirect('index')
				else:
					messages.error(request,"*Invalid User, Please Try Again & SignUp")
	context = {'formsign': form,}
	return render(request, 'sign.html', context)


def logoutUser(request):
	auth.logout(request)
	return redirect('index')