

"""
CountDown Timer

"""


import time
import os

mytime = int(input('Enter your time in seconds: '))

for x in range(mytime,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    os.system('cls')

print("Time is up!")
