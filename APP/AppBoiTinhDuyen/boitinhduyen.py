from tkinter import * 
from PIL import Image,ImageTk

win=Tk()
win.title("Bói Tình Duyên")
win.geometry("600x500")

load = Image.open('D:/Pictures/Untitled-1.png')
render = ImageTk.PhotoImage(load)
img = Label(win, image = render)
img.place(x=0,y=0)

def boi_tinh_yeu(ten_nam, ten_nu):
	#Chuyển thành viết thường
	ten_nam=ten_nam.lower()
	ten_nu=ten_nu.lower()
	#Chính
	dem=0
	#Chuyển bảng chữ cái thành số
	for bang_chu_cai in range(ord('a'), ord('z')+1):
		#tổng 2 số trùng nhau từ tên
		if (chr(bang_chu_cai) in ten_nam) and (chr(bang_chu_cai) in ten_nu):
			#Biến đểm để đếm các sỗ được lấy từ tên nam và tên nữ trùng nhau
			dem=dem+1

	#Bói
	if dem==0:
		ket_qua= "Không hợp nhau"
	elif dem <= 3:
		ket_qua= "Bạn bè"
	elif dem >= 4:
		ket_qua="Hợp nhau"
	else:
		ket_qua="Lỗi"
	return ket_qua

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)

def boi():
    INPUT = box.get(1.0,END)
    INPUT1 = box1.get(1.0,END)
    print(INPUT)
    print(INPUT1)
    a = boi_tinh_yeu(INPUT,INPUT1)
    kq.insert(END,a)

#đầu vào
label1=Label(win, text="Tên Nam", foreground="red", font=("Time New Roman", 20), bg="#EEDB99")
label1.pack()
box=Text(win,width=20,height=1,font=("ROBOTO",16))
box.pack()

label1=Label(win, text="Tên Nữ", foreground="red", font=("Time New Roman", 20), bg="#66D19D")
label1.pack(pady=18)
box1=Text(win,width=20,height=1,font=("ROBOTO",16))
box1.pack()


#Đầu ra
label1=Label(win, text="Kết Quả", foreground="red", font=("Time New Roman", 25), bg="#59C90D")
label1.pack()

kq=Text(win,width=20,height=1,font=("Arial",16))
kq.pack()

nutkq=Button(win, text="Kết Quả", bg="orange", fg="red", command=boi)
nutkq.pack(pady=20)

def clear1():
    kq.delete(1.0,END)

nutxoa=Button(win, text="Xoá kết quả", bg="orange", fg="red", command=clear1)
nutxoa.pack(pady=10)
nutxoakq=Button(win, text="Xoá Tên", bg="orange", fg="red", command=clear)
nutxoakq.pack(pady=1)



win.mainloop()