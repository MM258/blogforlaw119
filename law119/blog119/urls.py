from django.conf.urls.default import *
from blog119 import views

urlpatterns = patterns('',
	url(r'^$',views.home),
	url(r'^case/$',views.case),
	url(r'^blog/$',views.blog),
	url(r'^contact_us/$',views.contact_us),
	url(r'^about_us/$',views.about_us),
	)