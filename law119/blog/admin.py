from django.contrib import admin
from blog.models import Blog,Case,About_us,Contact_us


# Register your models here.
admin.site.register(Blog)
admin.site.register(Case)
admin.site.register(Contact_us)
admin.site.register(About_us)