from  tkinter import*
from tkinter.ttk import*
from time import strftime
a=Tk()
a.title('Đồng hồ đếm')
def clock():
    string=strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000, clock)
label=Label(a, font=("ALGER", 50), background='black', foreground='green')
label.pack(anchor='center')
clock()
a.mainloop()