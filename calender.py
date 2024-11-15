
from tkinter import*
import calendar

class Calendar:
	def __init__(self,root):
		self.root = root
		self.root.geometry("1100x2130+0+0")
		self.root.overrideredirect(True)
		
		self.frame = Frame(self.root,bg="white").place(x=0,y=0,height=2130,width=1100)
		
		self.lbl = Label(self.frame,text="CALENDER",bg="lime",font=("Arial",15,"bold")).place(x=350,y=40)
		
		self.lbl = Label(self.frame,text="Month",bg="white",font=("Arial",10)).place(x=100,y=250)
		self.lbl = Label(self.frame,text="Year",bg="white",font=("Arial",10)).place(x=850,y=250)
		self.spin1 = Spinbox(self.frame,bd=10,bg="lime",values=(1,2,3,4,5,6,7,8,9,10,11,12))
		self.spin1.place(x=100,y=320,width=200,height=100)
		self.spin2 = Spinbox(self.frame,bd=10,bg="lime",from_=1999,to_=2100,width=4)
		self.spin2.place(x=850,y=320,width=200,height=100)
		
		self.txt = Text(self.frame,bd=5,bg="lime")
		self.txt.place(x=330,y=550,height=400,width=500)
		
		self.btn = Button(self.frame,bd=7,bg="red",text="Show",font=("Arial",7,"bold"),command=self.show).place(x=500,y=1000,height=70,width=150)
		
	def show(self):
		a = int(self.spin1.get())
		b = int(self.spin2.get())
		
		cal = calendar.month(b,a)
		
		self.txt.delete(0.0,END)
		self.txt.insert(INSERT,cal)
		
root = Tk()
obj = Calendar(root)
root.mainloop()