from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 60)
	name = models.CharField(max_length = 30)
	blog_content = models.TextField()
	publition_date = models.DateField()

class Case(models.Model):
	# simage = models.ImageField()
	case_content = models.CharField(max_length = 250)

class About_us(models.Model):
	address = models.CharField(max_length = 30)

class Contact_us(models.Model):
	telephone = models.CharField(max_length = 15)

