from datetime import datetime


alarms = []


def add_alarm(alarm_time):
    alarms.append({
        "time": alarm_time,
        "enabled": True
    })


def delete_alarm(index):
    if 0 <= index < len(alarms):
        alarms.pop(index)


def toggle_alarm(index):
    if 0 <= index < len(alarms):
        alarms[index]["enabled"] = not alarms[index]["enabled"]


def check_alarms():
    current_time = datetime.now().strftime("%H:%M:%S")

    for alarm in alarms:
        if alarm["enabled"] and alarm["time"] == current_time:
            return True

    return False
