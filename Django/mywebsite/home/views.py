# Basic views for home app
from django.shortcuts import render

def home(request):
	context = {
		'title': 'Welcome to My Django Website',
		'intro': 'This is a simple demo site built with Django.'
	}
	return render(request, 'home/home.html', context)

def about(request):
	context = {
		'title': 'About This Website',
		'description': 'A tiny sample website showing Django templates, views and static files.'
	}
	return render(request, 'home/about.html', context)

def contact(request):
	contact_info = {
		'email': 'sample@example.com',
		'phone': '+92 300 1234567',
		'address': 'Lahore, Pakistan'
	}
	return render(request, 'home/contact.html', {'contact': contact_info})


# Create your views here.
