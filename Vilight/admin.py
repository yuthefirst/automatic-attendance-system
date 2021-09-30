from django.contrib import admin
from .models import * #import các models vào page admin
# Register your models here.

admin.site.register(Attendant) #Đăng ký models vào page admin
#admin.site.register(Axxxx)