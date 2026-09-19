import tkinter as tk
from datetime import datetime

from alarm_manager import add_alarm, alarms, check_alarms


root = tk.Tk()
root.title("Professional Alarm Clock")
root.geometry("500x500")


def update_clock():
    now = datetime.now()

    clock_label.config(
        text=now.strftime("%I:%M:%S %p")
    )

    date_label.config(
        text=now.strftime("%A, %d %B %Y")
    )

    if check_alarms():
        status_label.config(text="🔔 ALARM!")

    root.after(1000, update_clock)


def create_alarm():
    hour = hour_entry.get()
    minute = minute_entry.get()

    if not hour or not minute:
        status_label.config(text="Enter hour and minute")
        return

    alarm_time = f"{int(hour):02d}:{int(minute):02d}:00"

    add_alarm(alarm_time)

    alarm_list.insert(
        tk.END,
        alarm_time
    )

    status_label.config(
        text=f"Alarm set for {alarm_time}"
    )


clock_label = tk.Label(
    root,
    font=("Arial", 40, "bold")
)
clock_label.pack(pady=20)


date_label = tk.Label(
    root,
    font=("Arial", 16)
)
date_label.pack()


tk.Label(
    root,
    text="Set Alarm",
    font=("Arial", 18, "bold")
).pack(pady=20)


hour_entry = tk.Entry(root, width=5, font=("Arial", 16))
hour_entry.pack()


minute_entry = tk.Entry(root, width=5, font=("Arial", 16))
minute_entry.pack(pady=5)


tk.Button(
    root,
    text="Add Alarm",
    font=("Arial", 14),
    command=create_alarm
).pack(pady=10)


alarm_list = tk.Listbox(
    root,
    width=30,
    height=6,
    font=("Arial", 14)
)
alarm_list.pack(pady=10)


status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 12)
)
status_label.pack()


update_clock()

root.mainloop()
