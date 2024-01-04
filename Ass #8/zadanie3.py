import tkinter as tk
from tkinter import Label, StringVar
from datetime import datetime
from tkcalendar import Calendar

okno = tk.Tk()
okno.title("Zegar i Kalendarz")
okno.geometry("400x300")
okno.resizable(False, False)

date_time_var = StringVar()

def update_date_time():
    now = datetime.now()
    day = now.strftime('%d')
    month = now.strftime('%B')
    year = now.strftime('%Y')
    time = now.strftime('%H:%M:%S')
    day_of_week = now.strftime('%A')

    dt = f"{day_of_week}, {day} {month} {year}\n{time}"
    date_time_var.set(dt)
    date_time.after(1000, update_date_time)

date_time = Label(okno, textvariable=date_time_var, font=("Helvetica", 16))
date_time.pack(anchor="center")

cal = Calendar(okno, selectmode='day')
cal.pack(pady=20)

update_date_time()

okno.mainloop()
