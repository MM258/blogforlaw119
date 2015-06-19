from django.db import models

# Create your models here.


class Blog(models.Model):
	title = models.CharField(max_length = 60)
	name = models.CharField(max_length = 30)
	blog_content = models.TextField(max_length = 5000)
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
	
class JinjiManager(models.Manager):
	def get_queryset(self):
		return super(JinjiManager,self).get_queryset().filter(anli='J')

class XingshiManager(models.Manager):
	def get_queryset(self):
		return super(XingshiManager,self).get_queryset().filter(anli='X')

class Case(models.Model):
	case_image = models.ManyToManyField(Picture)
	case_content = models.CharField(max_length = 3000)
	anli = models.CharField(max_length = 1,choices = (('J','jinji'),('X','xingshi')))
	case = models.Manager()
	Jinji = JinjiManager()
	Xigshi = XingshiManager()


class About_us(models.Model):		
	context = models.TextField(max_length = 4000)
	myimage = models.ManyToManyField(Picture)

class Contact_us(models.Model):
	name = models.CharField(max_length = 30)
	company = models.CharField(max_length = 150)
	address = models.CharField(max_length = 50)
	telephone = models.CharField(max_length = 15)
	my_map = models.ManyToManyField(Picture)
	website = models.URLField()
	email = models.EmailField()