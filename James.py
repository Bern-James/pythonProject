from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

# Heading
Label(root, text="Registration Form", font="arial 15 bold").grid(row=0, column=3)

# Field name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
email = Label(root, text="Email")
paymentmood = Label(root, text="Paymentmood")

# Packing Fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
email.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

# Variable for storing data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emailvalue = StringVar
paymentmoodvalue = StringVar
checkvalue = IntVar

# Creating entry Field
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
emailentry = Entry(root, textvariable =emailvalue)
paymentmoodentry = Entry(root, textvariable =paymentmoodvalue)

# Packing for entry Field
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

# Creating CheckBox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

# Submit buttom
Button(text="Submit", command=getvals).grid(row=7, column=3)



root.mainloop()