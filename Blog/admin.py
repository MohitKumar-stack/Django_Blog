from django.contrib import admin
from Blog.models import Blogs,Message,USER_Data
# Register your models here.
admin.site.register(Blogs)
admin.site.register(Message)
admin.site.register(USER_Data)