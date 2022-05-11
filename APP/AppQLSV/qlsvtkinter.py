from tkinter import*
from tkinter.ttk import*
from tkinter import messagebox
import tkinter.scrolledtext as st
gd = Tk()
gd.title("Quản Lí Sinh Viên")
gd.geometry("900x500")

#Chức năng
class SinhVien():
    stt = ""
    name = ""
    ns = ""
    lop = ""
    khoa = ""
    def __init__(self,stt = "",name = "", ns = "",lop="" ,khoa = ""):
        self.stt = str(stt)
        self.name = str(name)
        self.ns = str(ns)
        self.lop = str(lop)
        self.khoa = str(khoa)
    def stt1(self):
        print("ID: ", self.stt)
    def hvt1(self):
        print("Họ Và Tên Của Sinh Viên là:", self.name)
    def ns1(self):
        print("Năm Sinh Của Sinh Viên=",self.ns)
    def lop1(self):
        print("Lớp Học Của Sinh Viên:",self.lop)
    def khoa1(self):
        print("Khoá Của Sinh Viên",self.khoa)

databasee = {
    "1" : ("..."),
    "2" : ("...")
}

#đầu vào
stt=Label(gd, text="STT", foreground = "red", font = ("Time New Roman", 15))
stt.place(x=700,y=20)

box = Text(gd,width = 20,height = 1,font = ("ROBOTO",16))
box.place(x=600,y=50)

tsv = Label(gd, text = "Tên Sinh Viên", foreground = "red", font = ("Time New Roman", 15))
tsv.place(x=664,y=90)

box1 = Text(gd,width = 20,height = 1,font = ("ROBOTO",16))
box1.place(x=600,y=120)

ns = Label(gd, text = "Năm Sinh", foreground = "red", font = ("Time New Roman", 15))
ns.place(x=680,y=160)

box2 = Text(gd,width = 20,height = 1,font = ("ROBOTO",16))
box2.place(x=600,y=190)

lop = Label(gd, text = "Lớp", foreground = "red", font = ("Time New Roman", 15))
lop.place(x=700,y=230)

box3 = Text(gd,width = 20,height = 1,font = ("ROBOTO",16))
box3.place(x=600,y=260)

khoa = Label(gd, text = "Khóa", foreground = "red", font = ("Time New Roman", 15))
khoa.place(x=697,y=300)

box4 = Text(gd,width = 20,height = 1,font = ("ROBOTO",16))
box4.place(x=600,y=330)

Label(gd, text = "Danh Sách Sinh Viên", font = ("Times New Roman", 15), background = 'green', foreground = "white").place(x=190,y=30)
text_area = st.ScrolledText(gd,width = 50, height = 10, font = ("Times New Roman",15))
text_area.place(x=30,y=60)
text_area.configure(state ='disabled')

def view_all():
    for stt, mean in databasee.items():
        print('[ %s: %s ]' % (stt, mean))
        text_area.insert(INSERT,' %s: %s  {}'.format("\n") % (stt, mean))
view_all()

def nhapten():
    stt = box.get(1.0,END)
    stt.strip("\n")
    hovaten = box1.get(1.0,END)
    hovaten.strip("\n")
    ns = box2.get(1.0,END)
    ns.strip("\n")
    lop = box3.get(1.0,END)
    lop.strip("\n")
    khoa = box4.get(1.0,END)
    khoa.strip("\n")
    class sv(SinhVien):
        pass
    mean = "{} ,{} ,{} ,{}".format(hovaten.strip("\n"),ns.strip("\n"),lop.strip("\n"),khoa.strip("\n"))
    databasee[stt.strip("\n")] = mean.strip("\n")
    sinhvienhoc = sv(stt.strip("\n"),hovaten.strip("\n"),ns.strip("\n"),lop.strip("\n"),khoa.strip("\n"))
    sinhvienhoc.stt1()
    sinhvienhoc.hvt1()
    sinhvienhoc.ns1()
    sinhvienhoc.lop1()
    sinhvienhoc.khoa1()
    messagebox.showinfo("Thông Báo", "Đã thêm sinh viên")


def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
    box2.delete(1.0,END)
    box3.delete(1.0,END)
    box4.delete(1.0,END)

nutthem=Button(gd, text="Thêm Sinh Viên", command = nhapten)
nutthem.place(x=675,y=380)

nutxoatatca=Button(gd, text="Xóa Phần Nhập", command = clear)
nutxoatatca.place(x=675,y=420)


def xoasv():
    gd2 = Tk()
    gd2.geometry("300x220")
    gd2.title("Xóa Sinh Viên")
    sott=Label(gd2, text="STT", foreground = "red", font = ("Time New Roman", 15))
    sott.pack()
    box = Text(gd2,width = 20,height = 1,font = ("ROBOTO",16))
    box.pack()
    def xoasv1():
        print(databasee)
        stt = box.get(1.0,END).strip("\n")
        if stt.strip("\n") in databasee:
            del databasee[stt.strip("\n")]
            print("Sinh Viên [ %s ] Đã Bị Xoá" % stt)
            messagebox.showinfo("Thông Báo", "Sinh Viên [ %s ] Đã Bị Xoá" % stt)
        else:
            print('Không Tìm Thấy Sinh Viên: [ %s ]' % stt)
            messagebox.showinfo("Thông Báo", "Không Tìm Thấy Sinh Viên: [ %s ]" % stt)
    
    nutxoa=Button(gd2, text="Xóa Sinh Viên", command = xoasv1)
    nutxoa.pack(pady=7)


def sxsv():
    def sx():
        items_sorted = sorted(databasee.items())
        for i in range(0,len(items_sorted)):
            print(items_sorted[i])
    sx()

def timsv():
    gd3 = Tk()
    gd3.geometry("300x120")
    gd3.title("Xóa Sinh Viên")
    TSV=Label(gd3, text="STT", foreground = "red", font = ("Time New Roman", 15))
    TSV.pack()
    box = Text(gd3,width = 20,height = 1,font = ("ROBOTO",16))
    box.pack()
    def find():
        stt = box.get(1.0,END).strip("\n")
        if stt in databasee:
            print("Đã Tìm Thấy Sinh Viên: [ %s: %s ]" % (stt, databasee[stt]))
            messagebox.showinfo("Thông Báo", "Đã Tìm Thấy Sinh Viên:\n [ %s: %s ]" % (stt, databasee[stt]))   
        else:
            print('Không Tìm Thấy Sinh Viên: [ %s ]' % stt)
            messagebox.showinfo("Thông Báo", "Không Tìm Thấy Sinh Viên:\n [ %s ]" % stt)

    nuttimsv=Button(gd3, text="Tìm Sinh Viên", command=find)
    nuttimsv.pack(pady=7)

#button

nutxoa=Button(gd, text="Xóa Sinh Viên", command = xoasv)
nutxoa.place(x=350,y=290)

nuttimsv=Button(gd, text="Tìm Sinh Viên", command=timsv)
nuttimsv.place(x=220,y=290)

nutsxsv=Button(gd,text="Sắp Xếp Sinh Viên", command=sxsv)
nutsxsv.place(x=70,y=290)

gd.mainloop()