from tkinter import *
from datetime import date

# Function to calculate age
def calculate_age():
    name = name_entry.get()
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        today = date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))
        message_label.config(text=f"Hello {name}, you are {age} years old!")
    except ValueError:
        message_label.config(text="Please enter valid numbers for date, month, and year.")

root = Tk()
root.title("age calculator")
root.geometry("400x400")

frame = Frame(master=root, height=200, width=360, bg="#d0efff")
frame.pack(pady=20)

# name
Label(frame, text="Name:", bg="#d0efff").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# day
Label(frame, text="Birthdate:", bg="#d0efff").grid(row=1, column=0, padx=10, pady=5, sticky="w")
day_entry = Entry(frame)
day_entry.grid(row=1, column=1, padx=10, pady=5)

# month
Label(frame, text="Birth month:", bg="#d0efff").grid(row=2, column=0, padx=10, pady=5, sticky="w")
month_entry = Entry(frame)
month_entry.grid(row=2, column=1, padx=10, pady=5)

# year
Label(frame, text="Birth year:", bg="#d0efff").grid(row=3, column=0, padx=10, pady=5, sticky="w")
year_entry = Entry(frame)
year_entry.grid(row=3, column=1, padx=10, pady=5)

#  button
calc_button = Button(root, text="Calculate Age", command=calculate_age, bg="#90ee90")
calc_button.pack(pady=10)

# message label
message_label = Label(root, text="", bg="#d0efff", font=("Arial", 12, "bold"))
message_label.pack(pady=20)

root.mainloop()