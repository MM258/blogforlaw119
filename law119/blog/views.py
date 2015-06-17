from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from blog.models import Blog,Contact_us,About_us
# Create your views here.
def home(request):
	# contact = Contact_us.objects.all()
	# return render_to_response('home.html',{"posts":contact},context_instance = RequestContext(request))
	
	return render_to_response('home.html','',context_instance = RequestContext(request))

def blog(request,spk):
	post = get_object_or_404(Blog, pk = pk)
	# post = get_object_or_404(Blog)
	return render_to_response("blog.html",{"posts": post},context_instance=RequestContext(request))

def case(request):
	# import ipdb;
	# ipdb.set_trace()
	return render_to_response('case.html','',context_instance = RequestContext(request))

def about_us(request):
	about = About_us.objects.all()
	return render_to_response('about_us.html',{"about":about},context_instance = RequestContext(request))

def contact_us(request):
	contact = Contact_us.objects.all()
	return render_to_response('contact_us.html',{"posts":contact},context_instance = RequestContext(request))
	