import time
import datetime
from dateutil import tz
from dateutil.parser import parse

alarm_input = input("What is the time that you want the alarm to go off in the following format: HH:MM:SS (AM/PM for 12 Hour Time)? ")
try:
    parsed_alarm = parse(alarm_input)
except Exception:
    print("Please remove AM/PM or change time to 12 hour clock.")
    exit()
alarm_utc = datetime.datetime.astimezone(parsed_alarm, tz=tz.UTC)
current_time = datetime.datetime.now(tz=tz.UTC)
if alarm_utc < current_time:
    print("Alarm time cannot be in the past, please re-enter")
    exit()
time_difference = alarm_utc-current_time
print(f"Alarm is set for: {alarm_utc}")
print(f"Current Time is: {current_time}")
print(f"Alarm is set for {time_difference} hours from now.")
while alarm_utc > current_time:
    time.sleep(1)
    current_time = datetime.datetime.now(tz=tz.UTC)
    continue
print("Alarm has triggered!!")
