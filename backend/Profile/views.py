from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import RegistrationForm, LoginForm

# Create your views here.

User = get_user_model()

def registration(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			phone_number = form.cleaned_data['phone_number']
			gender = form.cleaned_data['gender']

			new_user = User.objects.create_user(
				username=username,
				email=email,
				password=password,
				phone_number=phone_number,
				gender=gender
			)

			return redirect('login')
	else:
		form = RegistrationForm()

	context = {'form': form}
	return render(request, 'profile/registration.html', context)

def login(request):
	if request.method =='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				form.add_error(None, "wrong username or password")
	else:
		form = LoginForm()

	context = {'form': form}
	return render(request, 'profile/login.html', context)