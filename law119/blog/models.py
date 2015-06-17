from django.db import models

# Create your models here.


class Blog(models.Model):
	title = models.CharField(max_length = 60)
	name = models.CharField(max_length = 30)
	blog_content = models.TextField(max_length = 300)
	publition_date = models.DateField()
	
	class Meta:
		ordering = ['-id']
	
	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('post',(),{'pk':self.pk})


class Case(models.Model):
	# simage = models.ImageField()
	case_content = models.CharField(max_length = 250)

class About_us(models.Model):		
	context = models.TextField(max_length = 400)
	myimage = models.ImageField(upload_to = "photos")

class Contact_us(models.Model):
	name = models.CharField(max_length = 30)
	company = models.CharField(max_length = 150)
	address = models.CharField(max_length = 50)
	telephone = models.CharField(max_length = 15)
	mymap = models.ImageField(upload_to = "photos")
	website = models.URLField()
	email = models.EmailField()