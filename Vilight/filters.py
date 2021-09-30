import django_filters
from django.forms import ModelForm
from .models import *
#Tạo register và login form
from django.contrib.auth.forms import UserCreationForm #Sử dụng thư viện tạo người dùng
from django.contrib.auth.models import User #Thư viện hỗ trợ login
from datetime import date

class MyFilter(django_filters.FilterSet):   #Filter thẻ Home
    class Meta:
        model = Attendant
        fields = ('date', 'month', 'staff_id', 'name')


class MyForm(ModelForm): #Filter thẻ History, chỉ cho comment
    class Meta:
        model = Attendant
        fields = ('date','month', 'staff_id', 'name', 'comment')

class AdminForm(ModelForm): #Filter thẻ History, chỉ cho comment
    class Meta:
        model = Attendant
        fields = ('date','month', 'staff_id', 'name', 'comment','admin_comment')

class EditForm(ModelForm): #Filter thẻ Edit, cho tất cả các trường để chỉnh sửa được hoàn toàn
    class Meta:
        model = Attendant
        fields = '__all__'


class CreateUserForm(UserCreationForm):  #Fitler mặc định dùng hỗ trợ tạo User
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']