from django.http import HttpResponse
from django.shortcuts import redirect, render

#Phân bố sẵn các quyền ở đây, khi nào dùng thì gọi ra views

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated: #Nếu tài khoản đã đăng nhập thì cho vào tiếp thẻ home
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs) #Nếu chưa, trả về chức năng thẻ đó

	return wrapper_func

def allowed_users(allowed_roles=[]): #Vai trò cho phép
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name  #Lấy tên từ groups ra

			if group in allowed_roles: #Nếu groups có đủ vai trò
				return view_func(request, *args, **kwargs) #hiển thị chức năng tiếp theo
			else:
				return render(request,'Vilight/not-allowed.html')  #Không có trong allowed_roles, không cho vào
		return wrapper_func
	return decorator

