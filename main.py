import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Professional Alarm Clock")
root.geometry("500x400")


def update_clock():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)

    current_date = datetime.now().strftime("%A, %d %B %Y")
    date_label.config(text=current_date)

    root.after(1000, update_clock)


clock_label = tk.Label(
    root,
    text="12:00:00 AM",
    font=("Arial", 40, "bold")
)
clock_label.pack(pady=30)

date_label = tk.Label(
    root,
    text="Date",
    font=("Arial", 16)
)
date_label.pack()

update_clock()

root.mainloop()
