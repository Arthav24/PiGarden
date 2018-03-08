import os
import time

def sync():
    print("syncing time with RTC")
    time.sleep(2)
    try:
        os.system('sudo hwclock -w')
    except RuntimeError:
        print("Failed to Sync time,Check RTC")
        
    print(os.system('date;sudo hwclock -r'))

def currenttime():
    print(os.system('sudo hwclock -r'))

