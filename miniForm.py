from tkinter import *
from tkinter import messagebox


def getvals():
    print("Submitting form")
    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get(), foodservice.get()}")

    with open("record.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get(), foodservice.get()}\n")
        messagebox.showinfo("hello", "Inserted data successfully!!")


root = Tk()
root.geometry("500x500")
root.title("Mini Form!!!")
root.minsize(500, 500)
root.maxsize(500, 500)

lbl = Label(root, text="Welcom to Travels Form", font="comicsansms, 19 bold", bg="yellow", fg="red", relief="raised", bd="4")
lbl.pack()

namelbl = Label(root, text="Name :")
phonelbl = Label(root, text="Phone :")
genderlbl = Label(root, text="Gender :")
emergencylbl = Label(root, text="Emergency Contact :")
paymentlbl = Label(root, text="Payment Mode :")


namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
foodservice = IntVar()


nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry = Entry(root, textvariable=paymentvalue)

foodservicebtn = Checkbutton(root, text="want to prebookyour meals?", variable=foodservice)
foodservicebtn.place(x=100, y=260)

btn = Button(root, text="Submit", command=getvals)
btn.place(x=150, y=300)

namelbl.place(x=10, y=60)
nameentry.place(x=70, y=60)

phonelbl.place(x=10, y=100)
phoneentry.place(x=70, y=100)

genderlbl.place(x=10, y=140)
genderentry.place(x=70, y=140)

emergencylbl.place(x=10, y=180)
emergencyentry.place(x=130, y=180)

paymentlbl.place(x=10, y=220)
paymententry.place(x=110, y=220)


root.mainloop()

