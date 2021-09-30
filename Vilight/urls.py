from django.urls import path, include
from . import views
from django.contrib import admin


admin.site.site_header = "Vilight Administration"
admin.site.site_title = "Vilight Administration"
admin.site.index_title = "Home"


urlpatterns = [
    path('',views.home, name = 'home'),   #Đường dẫn đến view Home
    path('history/', views.history, name = 'history'), #Đường dẫn đến view History
    path('comment/<str:pk>/', views.comment, name = 'comment'),  #Đường dẫn đến view Comment có phụ thuộc id
    path('edit/', views.edit, name = 'edit'), #Đường dẫn đến view Edit
    path('edit_attendant/<str:pk>', views.edit_attendant, name = 'edit_attendant'), #Đường dẫn đến view edit_attendant có phụ thuộc id
    path('register/', views.registerPage, name = 'register'), #Đường dẫn đến trang Đăng ký
    path('login/', views.loginPage, name = 'login'), #Đường dẫn đến trang Đăng nhập
    path('logout/', views.logoutUser,name = 'logout'), #Đường dẫn khi bấm vào Logout sẽ trả về trang Đăng nhập
    path('export/',views.export_users_xls, name = 'export_excel'), #Đường dẫn để xuất file excel
    path('adminNe/',views.login, name = 'admin')

]