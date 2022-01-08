from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import pytz
import time
from datetime import datetime
root=Tk()
root.geometry("1000000x1000000")
root.title("Time and map")
map1=ImageTk.PhotoImage(Image.open("india.jpg"))
map2=ImageTk.PhotoImage(Image.open("usa.jpg"))
map3=ImageTk.PhotoImage(Image.open("australia.jpg"))
map4=ImageTk.PhotoImage(Image.open("japan.jpg"))

India_map1_image=Label(root)
India_map1_image["image"]=map1
India_map1_image.place(relx=0.2, rely=0.3, anchor=CENTER)
India=Label(root, text="India Time : ")
India.place(relx=0.1, rely=0.1, anchor=CENTER)

US_map2_image=Label(root)
US_map2_image["image"]=map2
US_map2_image.place(relx=0.5, rely=0.3, anchor=CENTER)
US=Label(root, text="U . S . A   Time : ")
US.place(relx=0.4, rely=0.1, anchor=CENTER)

Australia_map3_image=Label(root)
Australia_map3_image["image"]=map3
Australia_map3_image.place(relx=0.8, rely=0.3, anchor=CENTER)
Australia=Label(root, text="Australia Time : ")
Australia.place(relx=0.7, rely=0.1, anchor=CENTER)

Japan_map4_image=Label(root)
Japan_map4_image["image"]=map4
Japan_map4_image.place(relx=0.5, rely=0.7, anchor=CENTER)
Japan=Label(root, text="Japan Time : ")
Japan.place(relx=0.2, rely=0.7, anchor=CENTER)

resultUS=Label(root)
resultUS.place(relx=0.5, rely=0.1, anchor=CENTER)

resultaust=Label(root)
resultaust.place(relx=0.8, rely=0.1, anchor=CENTER)

resultIn=Label(root)
resultIn.place(relx=0.2, rely=0.1, anchor=CENTER)

resultjap=Label(root)
resultjap.place(relx=0.3, rely=0.7, anchor=CENTER)

class India_Time():
    def Times(self):
        Home=pytz.timezone('Asia/Kolkata')
        localtime=datetime.now(Home)
        currenttime=localtime.strftime("%H:%M:%S")
        resultIn["text"]="time: "+currenttime
        resultIn.after(200, self.Times)

class US_Time():
    def Times(self):
        Home=pytz.timezone('US/Central')
        localtime=datetime.now(Home)
        currenttime=localtime.strftime("%H:%M:%S")
        resultUS["text"]="time: "+currenttime
        resultUS.after(200, self.Times)

class Australia_Time():
    def Times(self):
        Home=pytz.timezone('Australia/ACT')
        localtime=datetime.now(Home)
        currenttime=localtime.strftime("%H:%M:%S")
        resultaust["text"]="time: "+currenttime
        resultaust.after(200, self.Times)

class Japan_Time():
    def Times(self):
        Home=pytz.timezone('Japan')
        localtime=datetime.now(Home)
        currenttime=localtime.strftime("%H:%M:%S")
        resultjap["text"]="time: "+currenttime
        resultjap.after(200, self.Times)

objectUS=US_Time()
objectIn=India_Time()
objectaust=Australia_Time()
objectjap=Japan_Time()
IndiaTime=Button(root, text="Show India Time", command=objectIn.Times)
IndiaTime.place(relx=0.2, rely=0.5, anchor=CENTER)
USTime=Button(root, text="Show   U . S . A   Time", command=objectUS.Times)
USTime.place(relx=0.5, rely=0.5, anchor=CENTER)
austTime=Button(root, text="Show Australia Time", command=objectaust.Times)
austTime.place(relx=0.8, rely=0.5, anchor=CENTER)
japTime=Button(root, text="Show Japan Time", command=objectjap.Times)
japTime.place(relx=0.5, rely=0.9, anchor=CENTER)


























root.mainloop()