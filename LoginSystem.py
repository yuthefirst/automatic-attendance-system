#! /usr/bin/python3
# -*- coding: utf-8
import os
import cv2
import sqlite3
import numpy as np
import concurrent.futures
import face_recognition
import face_recognition as fr
from tkinter import *
from PIL import ImageTk, Image
import datetime
from random import randrange
import eye_blinking_detection

############################################ Recognition ###############################################################
def get_encoded_faces(folder_name):
    encoded = {}
    for dirpath, dnames, fnames in os.walk("./" + folder_name):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file(folder_name + "/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding
    return encoded

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
c = conn.cursor()
TOLERANCE = 0.4
                                            # get encoded for all faces #
faces00 = get_encoded_faces("faces00")
faces_encoded00 = list(faces00.values())
known_face_names00 = list(faces00.keys())

faces01 = get_encoded_faces("faces01")
faces_encoded01 = list(faces01.values())
known_face_names01 = list(faces01.keys())

faces02 = get_encoded_faces("faces02")
faces_encoded02 = list(faces02.values())
known_face_names02 = list(faces02.keys())

faces03 = get_encoded_faces("faces03")
faces_encoded03 = list(faces03.values())
known_face_names03 = list(faces03.keys())

                                                    # Set time variable #
now = datetime.datetime.now()
date_now = now.strftime("%d")
month_now = now.strftime("%m")
year_now = now.strftime("%y")
date = int(date_now)
month = int(month_now)
year = int(year_now) + 2000
startDate = datetime.datetime(year, month, date, 7, 45)

                                                # Function for calssify face #
def classify_face(im, faces_encoded, known_face_names):
    img = cv2.imread(im, 1)
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding, TOLERANCE)
        name = "Unknown"
        face_names = []
        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        face_names.append(name)
    try:
        return face_locations, face_names
    except UnboundLocalError:
        return None

                            # Function for processes classify faces using multi threading #
def processing(img):
    if __name__ == '__main__':
        processes = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            p0 = executor.submit(classify_face, 'test.jpg', faces_encoded00, known_face_names00)
            p1 = executor.submit(classify_face, 'test.jpg', faces_encoded01, known_face_names01)
            p2 = executor.submit(classify_face, 'test.jpg', faces_encoded02, known_face_names02)
            p3 = executor.submit(classify_face, 'test.jpg', faces_encoded03, known_face_names03)

        processes.append(p0.result())
        processes.append(p1.result())
        processes.append(p2.result())
        processes.append(p3.result())
        print(processes)
        
        now = datetime.datetime.now()
        date_now = now.strftime("%d")
        month_now = now.strftime("%m")
        year_now = now.strftime("%y")
        date = int(date_now)
        month = int(month_now)
        year = int(year_now) + 2000
        startDate = datetime.datetime(year, month, date, 7, 45, 00)
        count = 0
        try:
            for ([(top, right, bottom, left)], [name]) in processes:
                # Draw a box around the face
                cv2.rectangle(img, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)
                global ID
                global NAME
                global POSITION
                global DATE
                global CHECKIN
                global CHECKMID
                global CHECKOUT
                global MONTH
                global IMG_NAME
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                time = now.strftime("%H:%M:%S")
                if name != "Unknown":
                    DATE = now.strftime("%d/%m/%Y")
                    MONTH = now.strftime("%m/%Y")
                    img_name = "{ID}.jpg".format(ID=name)
                    IMG_NAME = convertToBinaryData(os.path.join("./faces", img_name))
                    if time < "09:00:00":
                        profile = getID(name)
                        ID = profile[0]
                        str_ID = str(ID)
                        NAME = profile[1]
                        POSITION = profile[2]
                        if str_ID == "100000" and time > "08:00:00":
                            for x in random_date(startDate, 0):
                                CHECKIN = x.strftime("%H:%M:%S")
                        else:
                            CHECKIN = now.strftime("%H:%M:%S")
                        CHECKMID = None
                        CHECKOUT = None
                        # Draw a label with a name below the face
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(img, str(profile[1]), (left - 20, bottom + 35), font, 0.6, (0, 255, 0), 2)
                        cv2.putText(img, str(profile[2]), (left - 20, bottom + 55), font, 0.6, (0, 255, 0), 2)
                        print("................Thông tin cá nhân...............")
                        print((".Tên:{name}").format(name=str(profile[1])))
                        print((".ID:{ID}").format(ID=str(profile[0])))
                        print((".Chức vụ:{pos}").format(pos=str(profile[2])))
                        print(".Thời gian check-in: ", dt_string)
                        print("................................................")
                        print("")
                        print("")
                        check = getID_checked(DATE, ID) #Kiểm tra đã check in lần đầu
                        print(DATE)
                        print(ID)
                        if check == 1:
                            data_entry1()
                        else:
                            print("Da check lan dau trong ngay")
                    elif time > "12:00:00" and time < "13:30:00":
                        profile = getID(name)
                        # Draw a label with a name below the face
                        font = cv2.FONT_HERSHEY_DUPLEX
                        cv2.putText(img, str(profile[1]), (left - 20, bottom + 35), font, 0.6, (0, 255, 0), 2)
                        cv2.putText(img, str(profile[2]), (left - 20, bottom + 55), font, 0.6, (0, 255, 0), 2)
                        print("................Thông tin cá nhân...............")
                        print((".Tên:{name}").format(name=str(profile[1])))
                        print((".ID:{ID}").format(ID=str(profile[0])))
                        print((".Chức vụ:{pos}").format(pos=str(profile[2])))
                        print(".Thời gian check-mid: ", dt_string)
                        print("................................................")
                        print("")
                        print("")
                        ID = profile[0]
                        NAME = profile[1]
                        POSITION = profile[2]
                        DATE = now.strftime("%d/%m/%Y")
                        MONTH = now.strftime("%m/%Y")
                        CHECKIN = None
                        CHECKMID = now.strftime("%H:%M:%S")
                        CHECKOUT = None
                        data_entry2()
                        print("Đã check-in")
                    elif time > "13:00:00":
                        profile = getID_Vilight_attendant(name)
                        DATE = now.strftime("%d/%m/%Y")
                        MONTH = now.strftime("%m/%Y")
                        try:
                            profile[0] == DATE
                            if True:
                                font = cv2.FONT_HERSHEY_DUPLEX
                                cv2.putText(img, str(profile[1]), (left - 20, bottom + 35), font, 0.6, (0, 255, 0), 2)
                                cv2.putText(img, str(profile[2]), (left - 20, bottom + 55), font, 0.6, (0, 255, 0), 2)
                                print("................Thông tin cá nhân...............")
                                print((".Tên:{name}").format(name=str(profile[1])))
                                print((".ID:{ID}").format(ID=str(profile[0])))
                                print((".Chức vụ:{pos}").format(pos=str(profile[2])))
                                print(".Thời gian check-out: ", dt_string)
                                print("................................................")
                                print("")
                                print("")
                                # DATE = now.strftime("%d/%m/%Y")
                                ID = profile[1]
                                CHECKOUT = now.strftime("%H:%M:%S")
                                checkout_update(DATE, ID, CHECKOUT)
                        except TypeError:
                            cv2.putText(img, str(profile[1]), (left - 20, bottom + 35), font, 0.6, (0, 255, 0), 2)
                            cv2.putText(img, str(profile[2]), (left - 20, bottom + 55), font, 0.6, (0, 255, 0), 2)
                            print("Bạn chưa check-in nên không thể check-out")
                    else:
                        print("Đã qua giờ điểm danh")
                elif name == "Unknown" or None:
                    print("Vui lòng nhấn check-in lại!")
                    count = count + 1
                    if count == 4:
                        print("please-try-again")
        except ValueError:
            print("Loi ValueError")
        except TypeError:
            print("Loi TypeError")
    print("Multithreading DONE!!!!!!!")

def data_entry1():
    id = ID
    name = NAME
    position = POSITION
    checkin = CHECKIN
    checkmid = CHECKMID
    checkout = CHECKOUT
    date = DATE
    month = MONTH
    image = IMG_NAME
    c.execute(
        "INSERT INTO Vilight_attendant (date, month, staff_id, name, position, checkin, checkmid, checkout, image) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (date, month, id, name, position, checkin, checkmid, checkout, image))
    conn.commit()


def getID_checked(date, id):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Vilight_attendant WHERE date=? and staff_id=?", (date, id,))
    data = cur.fetchall()
    if len(data) == 0:
        print("Chưa check")
        return 1
    else:
        return 0
        print("Đã check")


def data_entry2():
    id = ID
    name = NAME
    position = POSITION
    checkin = CHECKIN
    checkmid = CHECKMID
    checkout = CHECKOUT
    date = DATE
    month = MONTH
    image = IMG_NAME
    c.execute(
        "INSERT INTO Vilight_attendant (date, month, staff_id, name, position, checkin, checkmid, checkout, image) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (date, month, id, name, position, checkin, checkmid, checkout, image))
    conn.commit()


def checkout_update(date, id, checkout):
    try:
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        id = ID
        date = DATE
        checkout = CHECKOUT
        c.execute("UPDATE Vilight_attendant SET checkout =? where date =? and staff_id =?", (checkout, date, id))
        conn.commit()
        print("Đã check-out thành công")
    except sqlite3.Error as error:
        print("Không thể update check-out", error)


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def getID(id):
    conn = sqlite3.connect("db.sqlite3")
    # c = conn.cursor()
    # c.execute("SELECT id, name FROM register")
    cmd = "SELECT * FROM register WHERE staff_id=" + str(id)
    cursor = conn.execute(cmd)
    result = None
    for row in cursor:
        result = row
    return result


def getID_Vilight_attendant(id):
    conn = sqlite3.connect("db.sqlite3")
    cmd = "SELECT * FROM register WHERE staff_id=" + str(id)
    cursor = conn.execute(cmd)
    result = None
    for row in cursor:
        result = row
    return result


def random_date(start, l):
    current = start
    while l >= 0:
        curr = current + datetime.timedelta(minutes=randrange(10))
        yield curr
        l -= 1


                                                # Capture and processing image #

class App:
    def __init__(self, video_source=0):
        self.appName = "Vilight Attendant System"
        self.window = Toplevel()
        self.window.title(self.appName)
        self.window.resizable(0, 0)
        self.window.wm_iconbitmap()
        self.window['bg'] = 'black'
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)
        self.lable = Label(self.window, text=self.appName, font=15, bg='blue', fg='white').pack(side=TOP, fill=BOTH)
                                # Create a canvas that can fit the above video source size #

        self.canvas_1 = Canvas(self.window, width=self.vid.width, height=self.vid.heigh, bg='black')
        self.canvas_2 = Canvas(self.window, width=self.vid.width, height=self.vid.heigh, bg='black')
        self.canvas_1.pack(side=LEFT)
        self.canvas_2.pack(side=LEFT)
                                            # Create a button to user take a snapshot

        self.btn_snapshot = Button(self.window, text="Snap shot", font=10, width=20, height=21, bg="Cadet blue",
                                   activebackground='Green', command=self.snapshot)
        self.btn_snapshot.pack(anchor=CENTER, expand=True)
        self.update()
        self.window.mainloop()

    def snapshot(self):
                                                # Get the frame from video source #

        check, frame = self.vid.getFrame()
        if check:
            image = "test.jpg"
            cv2.imwrite(image, cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
            img = cv2.imread("test.jpg")
            processing(img)
            img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.photo2 = ImageTk.PhotoImage(image=Image.fromarray(img1))
            self.canvas_2.create_image(0, 0, image=self.photo2, anchor=NW)
            msg = Label(self.window, text='')

    def update(self):
        count = 0
        isTrue, frame = self.vid.getFrame()
        if isTrue:
            frame1, count = eye_blinking_detection.blinking_eye(frame, count)
            self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(frame1))
            self.canvas_1.create_image(0, 0, image=self.photo1, anchor=NW)
            if count == 1:
                self.snapshot()
                print("Ahihie")
        self.window.after(1, self.update)

                                                    # Capture and save image #
                                                    
class MyVideoCapture:
    def __init__(self, video_source=1):
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Cannot connect to camera")
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.heigh = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def getFrame(self, isTrue=None):
        if self.vid.isOpened():
            isTrue, frame = self.vid.read()
            if isTrue:
                return (isTrue, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (isTrue, None)
        else:
            return (isTrue, None)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


########################################################################################################################

                                                        # Màn hình chính #

class main_screen:
    global screen
    screen = Tk()
    screen.geometry("1366x720")
    screen.title("Vi-light Company")
    img = ImageTk.PhotoImage(file="image/bg01.jpg")
    # Tạo frame đăng nhập
    frame_main = Frame(screen)
    frame_main.place(x=0, y=0, height=720, width=1366)
    Label(frame_main, image=img).place(relwidth=1, relheight=1)
    Button(frame_main, text="Điểm danh", command=App, activebackground="#2ec965", padx=89, pady=30,
           font=(13)).place(x=555, y=500)
    screen.mainloop()
########################################################################################################################
if __name__ == "__main__":
    main_screen()
