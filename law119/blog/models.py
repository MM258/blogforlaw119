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

	# @models.permalink
	# def get_absolute_url(self):
	# 	return ('post',(),{'pk':self.pk})
class Picture(models.Model):
	title = models.CharField(max_length = 20)
	image = models.ImageField(upload_to = "photos")

	def __unicode__(self):
		return self.title
	

class Case(models.Model):
	case_image = models.ForeignKey(Picture)
	gender_choices = (('J','jinji'),('X','xingshi'))
	case_content = models.CharField(max_length = 250)
	anli = models.CharField(max_length = 1,choices = gender_choices)

class About_us(models.Model):		
	context = models.TextField(max_length = 400)
	myimage = models.ForeignKey(Picture)

class Contact_us(models.Model):
	name = models.CharField(max_length = 30)
	company = models.CharField(max_length = 150)
	address = models.CharField(max_length = 50)
	telephone = models.CharField(max_length = 15)
	my_map = models.ForeignKey(Picture)
	website = models.URLField()
	email = models.EmailField()