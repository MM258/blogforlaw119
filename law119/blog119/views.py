from django.shortcuts import render_to_response

def home(request):
	return render_to_response('home.html')

def blog(request):
	return render_to_response('blog.html')

def about_us(request):
	return render_to_response('about_us.html')

def case(request):
	return render_to_response('case.html')

def contact_us(request):
	return render_to_response('contact_us.html')

