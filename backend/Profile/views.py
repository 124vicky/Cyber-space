from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from .forms import RegistrationForm

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

			return redirect('success')
	else:
		form = RegistrationForm()

	context = {'form': form}
	return render(request, 'profile/registration.html', context)