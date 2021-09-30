#! /usr/bin/python3
# -*- coding: utf-8
from tkinter import *
import os
from tkinter import messagebox
from PIL import ImageTk, Image
import cv2
import sqlite3

def delete1():
    screen1.destroy()

def delete2():
    screen2.destroy()

def delete3():
    screen3.destroy()


#Sai mật khẩu
def password_not_recognised():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Cảnh báo")
    screen2.geometry("300x100")
    Label(screen2,text = "").pack()
    Label(screen2, text="Sai mật khẩu!!",fg = "red").pack()
    Button(screen2, text="OK", command=delete2,width = 10 ).pack()

#Khi không tìm thấy người dùng
def user_not_found():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Cảnh báo")
    screen3.geometry("300x100")
    # Label(screen3,text = "").pack()
    Label(screen3, text="Người dùng không khả dụng!!",fg ="Red").pack()
    Button(screen3, text="OK", command=delete3, width = 10).pack()

#Login verify
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            register_screen()                              #Đăng nhập thành công thì cho đăng ký
        else:
            password_not_recognised()
    else:
        user_not_found()

##login screen
def login_screen():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("1366x720")
    screen1.title("Vi-Light Register System")
    # Tạo frame login
    img1 = ImageTk.PhotoImage(file = "image/bg01.jpg")
    frame_login = Frame(screen1)
    frame_login.place(x=0, y=0, width=1366, height=720)


    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1


    Label(frame_login, text="HỆ THỐNG ĐĂNG KÝ THÔNG TIN NHÂN VIÊN", bg="cadet blue", width="300", height="5", font=("Calibri", 13,"bold")).pack()
    Label(frame_login, text = "VUI LÒNG ĐĂNG NHẬP ĐỂ TIẾP TỤC", font = ("Calibri", 13, "bold"), fg ="green").place(x= 560, y=180)
    Label(frame_login, text="Tài khoản",font = (13)).place(x=648,y=250)
    username_entry1 = Entry(frame_login, textvariable=username_verify, font = (13))
    username_entry1.place(x=560, y=280,width = 250,height = 30)

    Label(frame_login, text="Mật khẩu",font = (13)).place(x = 650, y = 330)
    password_entry1 = Entry(frame_login, textvariable=password_verify, show = "*",font = (13))
    password_entry1.place(x=560, y=360,width = 250,height = 30)

    Button(frame_login, text="Đăng nhập", width="30", height="2", command=login_verify,activebackground = "#2ec965", font = (13),borderwidth = 3).place(x=545, y=430)
    Button(frame_login,text ="Trở lại", height="2", width="30", command= delete1,activebackground = "#2ec965",font = (13),borderwidth = 3).place(x=545, y=510)

#Confirm to Exit
def iExit():
    answer = messagebox.askquestion("Confirm exit", "Bạn thật sự muốn tắt chương trình?")
    if answer == "yes":
        screen.quit()

############################################## register ################################################################
########################################################################################################################
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

#Chức năng điểm danh, check in or out
def register_screen():
    global screen7
    global ID
    global NAME
    global POSITION
    global IMG_NAME
    global ID_entry
    global NAME_entry
    global POSITION_entry


    screen7 = Toplevel(screen)
    screen7.title("Register Screen")
    screen7.geometry("1366x720")
    screen1.withdraw() #Thoát màn hình đăng nhập
    heading = Label(screen7, text = "VUI LÒNG ĐIỀN ĐẦY ĐỦ THÔNG TIN", bg = "cadet blue", fg = "black", font = ("Calibri", 13, "bold"))
    heading.place(x = 0, y = 0, width = 1366, height = 100)

    sub = Label(screen7,text = "LƯU Ý GHI KHÔNG DẤU", fg = "green", font = ("Calibri",13, "bold"))
    sub.place(x = 0, y = 120,width = 1366)


    # Đăng ký thông tin cá nhân
    ID = StringVar()
    NAME = StringVar()
    POSITION = StringVar()

    # Tạo ngõ vào trong màn hình đăng ký
    ID_entry = Entry(screen7, textvariable=ID, font=13, width=30)
    NAME_entry = Entry(screen7, textvariable=NAME, font=13, width=30)
    POSITION_entry = Entry(screen7, textvariable=POSITION, font=13, width=30)

    #Nút lưu thông tin
    btn_register = Button(screen7, text = "ĐĂNG KÝ",command = saveee, borderwidth = 3, font = ("Calibri",13,"bold"), width = 40, height = 2)
    btn_register.place(x=500, y=600)

    #Nút đăng ký thông tin hình ảnh
    btn_capture = Button(screen7, text = "CHỤP ẢNH",command = capture_img, font = ("Calibri",13,"bold"), borderwidth = 3, width = 40, height = 2)
    btn_capture.place(x = 500, y = 520)


    idlabel = Label(screen7,text = "ID", font = 15, width = 30)
    namelabel = Label(screen7, text = "Họ và tên", font = 15, width = 30)
    positionlabel = Label(screen7, text = "Vị trí (Chức vụ)", font = 15, width = 30)


    ID_entry.place(x=550, y=230, height = 40)
    NAME_entry.place(x=550, y=330, height = 40)
    POSITION_entry.place(x = 550, y = 430, height = 40)
    idlabel.place(x=550, y=200)
    namelabel.place(x=550, y = 300)
    positionlabel.place(x=550, y=400)


#Lệnh chụp ảnh
def capture_img():
    global IMG_NAME
    cam = cv2.VideoCapture(1)
    # cam.set(3, 1400)
    # cam.set(4, 720)
    while True:
        # CAPTURE IMAGE
        ret, frame = cam.read()
        if not ret:
            print("Không thể kết nối camera")
            break
        cv2.imshow("Camera", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Đã nhấn ESC, thoát. . .")
            break
        elif k % 256 == 32:
            # SPACE pressed
            # .get()  để lấy dữ liệu từ khung nhập dữ liệu
            img_name = "{ID}.jpg".format(ID=ID.get())
            cv2.imwrite(os.path.join("./faces", img_name), frame)
            print("Hình của {} đã được ghi!".format(img_name))
            break

    ##Tắt camera sau khi chụp
    cv2.destroyWindow("Camera")
    cam.release()
    IMG_NAME = convertToBinaryData(os.path.join("./faces", img_name))
    create_table()
    data_entry1()
    c.close()
    conn.close()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS register(id INT, name TEXT, position TEXT, image BLOB)')

def data_entry1():
    create_table()
    id = ID.get()
    name = NAME.get()
    position = POSITION.get()
    image = IMG_NAME
    c.execute("INSERT INTO register (staff_id, name, position, image) VALUES(?, ?, ?, ?)", (id, name, position, image))
    conn.commit()

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
def saveee():
    ID_entry.delete(0, END)
    NAME_entry.delete(0, END)
    POSITION_entry.delete(0,END)


####################################################Màn hình chính######################################################
########################################################################################################################
class main_screen:
    global screen
    screen = Tk()
    screen.geometry("1366x720")
    screen.title("Vi-light Company")

    img = ImageTk.PhotoImage(file = "image/bg01.jpg")
    #Tạo frame đăng nhập
    frame_main = Frame(screen)
    frame_main.place(x=0, y=0, height=720, width=1366)
    Label(frame_main, image=img).place(relwidth=1, relheight=1)


    Button(frame_main, text = "Đăng ký", command = login_screen,activebackground = "#2ec965",padx = 98,pady = 30,
           font = (13)).place(x = 555, y = 500)


    screen.mainloop()

if __name__ == "__main__":
    main_screen()