from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		name = request.POST['full-name']
		email = request.POST['email']
		sayhello = request.POST['sayhello']

		return render(request, 'contact.html', {'name': name})
	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html')