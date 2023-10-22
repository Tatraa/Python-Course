import datetime
import time

while True:
    now = datetime.datetime.now()
    hours = str(now.hour).zfill(2)
    minutes = str(now.minute).zfill(2)
    seconds = str(now.second).zfill(2)
    clock = f"► {hours}:{minutes}:{seconds} ◄"
    print(clock, end='\r')
    time.sleep(0.5)
