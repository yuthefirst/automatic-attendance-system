from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  #thư viện xác minh, đăng nhập, đăng xuất
from django.contrib.auth.decorators import login_required #Thư viện yêu cầu đăng nhập
from .decorators import unauthenticated_user, allowed_users  #import thư vien
import xlwt
import datetime
from django.contrib.auth.models import Group
# Create your views here.

@login_required(login_url='login')  #Yêu cầu đăng nhập nè
def home(request):
    attendant = Attendant.objects.all()   #Lấy tất cả objects trong model Attendant
    myFilter = MyFilter(request.GET, queryset=attendant)  #Query attendant qua bộ lọc MyFilter
    myFilter.qs #Kết quả xử lý nằm ở đây

   # print(myFilter.qs)  #Check kết quả ở terminal

    context = {'attendant': attendant, 'myFilter':myFilter}
    return render(request, 'Vilight/home.html', context)


@login_required(login_url='login')  #Yêu cầu đăng nhập nè
def history(request):
    attendant = Attendant.objects.all()
    myFilter = MyFilter(request.GET, queryset=attendant)
    myFilter.qs

    context = {'attendant': attendant, 'myFilter': myFilter}
    return render(request, 'Vilight/history.html', context)


@login_required(login_url='login')  #Yêu cầu đăng nhập nè
def comment(request, pk):
    attendant = Attendant.objects.get(id=pk)
    form = MyForm(instance=attendant)
    if request.method == "POST":
        form = MyForm(request.POST,instance=attendant)
        if form.is_valid():
            form.save()
            return redirect('/history')
    context = {'form':form}
    return render(request, 'Vilight/comment.html',context)


@allowed_users(allowed_roles=['Admin']) #Gọi tên groups được truy cập vào view này
@login_required(login_url='login')  #Yêu cầu đăng nhập nè
def edit_attendant(request,pk):
    attendant = Attendant.objects.get(id=pk)
    form = EditForm(instance=attendant)
    if request.method == "POST":
        form = EditForm(request.POST, instance=attendant)
        if form.is_valid():
            form.save()
            return redirect('/edit')  #Sau khi chỉnh sửa xong, trả về thẻ EDIT
    context = {'form': form}
    return render(request, 'Vilight/admincomment.html',context)  #Vì dùng chung cấu trúc nên chỉ cần gọi lại thẻ html


@allowed_users(allowed_roles=['Admin']) #Gọi tên groups được truy cập vào view này
@login_required(login_url='login')  #Yêu cầu đăng nhập nè
def edit(request):
    attendant = Attendant.objects.all()
    myFilter = MyFilter(request.GET, queryset=attendant)
    myFilter.qs

    context = {'attendant': attendant, 'myFilter': myFilter}
    return render(request, 'Vilight/edit.html', context)


@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated: #Nếu đã đăng nhập thì sẽ trở về thẻ home
        return redirect('home')
    else:
        form = CreateUserForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name = 'Staff')  #Mới tạo sẽ add vào Group Customer
                user.groups.add(group)

                messages.success(request, 'Tạo thành công tài khoản ' + username)
                return redirect('login')

        context = {'form':form}
        return render(request, 'Vilight/register.html',context)


@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:  # Nếu đã đăng nhập thì sẽ trở về thẻ home
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password) #lệnh dùng để xác minh

            if user is not None: #Nếu có user thì trả về trang 'home'
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Tài khoản hoặc mật khẩu không đúng!')
        context = {}
        return render(request, 'Vilight/login.html',context)


def logoutUser(request):
    logout(request) #Sử dụng trực tiếp thư viện để Đăng xuất
    return redirect('login')


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename= Vilight_report ' + str(datetime.date.today()) +' .xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Attendant List') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['NGÀY', 'MÃ NHÂN VIÊN', 'HỌ VÀ TÊN','VỊ TRÍ', 'CHECK IN', 'CHECK MID', 'CHECK OUT', 'COMMENT', 'PHÊ DUYỆT' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    attendant = Attendant.objects.all()
    myFilter = MyFilter(request.GET, queryset=attendant)
    myFilter.qs

    rows = myFilter.qs.values_list('date','staff_id','name','position','checkin', 'checkmid', 'checkout','comment','admin_comment')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response