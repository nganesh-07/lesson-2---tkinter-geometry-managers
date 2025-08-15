from tkinter import *

# window
root = Tk()
root.title("login app")
root.geometry("400x400")

# create a frame
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# add widgets and label
lb11 = Label(frame, text="full name", bg="#3895D3", fg="white", width=12)
lb12 = Label(frame, text="email ID", bg="#3895D3", fg="white", width=12)
lb13 = Label(frame, text="enter password", bg="#3895D3", fg="white", width=12)

# use entry widget to create textbox
entryname = Entry(frame)
entryemail = Entry(frame)
entrypass = Entry(frame, show="*")

# function to display message
def display():
    name = entryname.get()
    greet = "Hey", name
    message = "You've created your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

# textbox to display message
textbox = Text(bg="#BEBEBE", fg="black")

# add a button
btn = Button(text = "create account", command=display, bg="red")

# arrange the widgets
frame.place(x=20, y=0)
lb11.place(x=20, y=20)
entryname.place(x=150, y=20)
lb12.place(x=20, y=80)
entryemail.place(x=150, y=80)
lb13.place(x=20, y=140)
entrypass.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()