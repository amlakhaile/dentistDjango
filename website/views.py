from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		name = request.POST['full-name']
		email = request.POST['email']
		sayhello = request.POST['sayhello']

		#send an email
		send_mail(
			name,#subject
			sayhello,#message
			email,#from email
			['amlakhaile@gmail.com'],#to email
			)

		return render(request, 'contact.html', {'name': name})
	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html')