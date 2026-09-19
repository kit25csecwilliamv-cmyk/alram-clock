import tkinter as tk
from datetime import datetime

from alarm_manager import (
    add_alarm,
    alarms,
    delete_alarm,
    toggle_alarm,
    check_alarms
)

from sound_manager import play_alarm, stop_alarm


# --------------------------------------------------
# VARIABLES
# --------------------------------------------------

alarm_ringing = False
current_ringing_alarm = None


# --------------------------------------------------
# MAIN WINDOW
# --------------------------------------------------

root = tk.Tk()

root.title("Professional Alarm Clock")
root.geometry("550x600")

root.resizable(False, False)


# --------------------------------------------------
# CLOCK
# --------------------------------------------------

clock_label = tk.Label(
    root,
    text="12:00:00 AM",
    font=("Arial", 42, "bold")
)

clock_label.pack(pady=25)


# --------------------------------------------------
# DATE
# --------------------------------------------------

date_label = tk.Label(
    root,
    text="Date",
    font=("Arial", 16)
)

date_label.pack()


# --------------------------------------------------
# ALARM INPUT
# --------------------------------------------------

tk.Label(
    root,
    text="Set Alarm",
    font=("Arial", 20, "bold")
).pack(pady=20)


input_frame = tk.Frame(root)

input_frame.pack()


tk.Label(
    input_frame,
    text="Hour"
).grid(row=0, column=0)


tk.Label(
    input_frame,
    text="Minute"
).grid(row=0, column=1)


hour_entry = tk.Entry(
    input_frame,
    width=8,
    font=("Arial", 16),
    justify="center"
)

hour_entry.grid(
    row=1,
    column=0,
    padx=5
)


minute_entry = tk.Entry(
    input_frame,
    width=8,
    font=("Arial", 16),
    justify="center"
)

minute_entry.grid(
    row=1,
    column=1,
    padx=5
)


# --------------------------------------------------
# ADD ALARM
# --------------------------------------------------

def create_alarm():

    hour = hour_entry.get().strip()
    minute = minute_entry.get().strip()

    try:

        hour = int(hour)
        minute = int(minute)

        if hour < 0 or hour > 23:
            raise ValueError

        if minute < 0 or minute > 59:
            raise ValueError

    except ValueError:

        status_label.config(
            text="Enter valid time: HH and MM"
        )

        return

    alarm_time = f"{hour:02d}:{minute:02d}:00"

    add_alarm(alarm_time)

    refresh_alarm_list()

    hour_entry.delete(0, tk.END)
    minute_entry.delete(0, tk.END)

    status_label.config(
        text=f"Alarm added: {alarm_time}"
    )


add_button = tk.Button(
    root,
    text="➕ Add Alarm",
    font=("Arial", 14, "bold"),
    command=create_alarm,
    width=18
)

add_button.pack(pady=15)


# --------------------------------------------------
# ALARM LIST
# --------------------------------------------------

tk.Label(
    root,
    text="My Alarms",
    font=("Arial", 18, "bold")
).pack(pady=5)


alarm_list = tk.Listbox(
    root,
    width=35,
    height=8,
    font=("Arial", 14)
)

alarm_list.pack(pady=10)


# --------------------------------------------------
# REFRESH ALARM LIST
# --------------------------------------------------

def refresh_alarm_list():

    alarm_list.delete(0, tk.END)

    for alarm in alarms:

        state = "ON" if alarm["enabled"] else "OFF"

        alarm_list.insert(
            tk.END,
            f"{alarm['time']}    [{state}]"
        )


# --------------------------------------------------
# DELETE
