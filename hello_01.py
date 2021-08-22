from tkinter import *
from datetime import date

root = Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("TWY Age Calculator")

lbl_title = Label(text="AGE CALCULATOR", font=('arial', 50, 'bold'), foreground='fuchsia')
lbl_title.pack()

Label(text="Name", font=23).place(x=200, y=250)
Label(text="Year", font=23).place(x=200, y=300)
Label(text="Month", font=23).place(x=200, y=350)
Label(text="Date", font=23).place(x=200, y=400)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dateValue = StringVar()

nameEntry = Entry(root, textvariable = nameValue, width = 30, bd = 3, font=20)
nameEntry.place(x=300, y = 250)
yearEntry = Entry(root, textvariable = yearValue, width = 30, bd = 3, font=20)
yearEntry.place(x=300, y = 300)
monthEntry = Entry(root, textvariable = monthValue, width = 30, bd = 3, font=20)
monthEntry.place(x=300, y = 350)
dateEntry = Entry(root, textvariable = dateValue, width = 30, bd = 3, font=20)
dateEntry.place(x=300, y = 400)

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day)<(birthDate.month, birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}", font=30).place(x = 300, y = 500)

Button(text="Calculate Age", font=20, bg="black", fg="white", width = 11, height=2, command=calculateAge).place(x=300, y=450)

root.mainloop()