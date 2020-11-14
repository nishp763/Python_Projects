import time # for getting time
from playsound import playsound # for playing audio file
import os # for getting sound file path
import sched # for scheduling events

def set_alarm(set_time, sound_file, message):
    myscheduler = sched.scheduler(time.time, time.sleep) # create a scheduler instance
    myscheduler.enterabs(set_time, 1, print, argument=(message,)) # schedule to print message at alarm time
    myscheduler.enterabs(set_time, 1, playsound, argument=(sound_file,)) # schedule to play .wav file at alarm time
    print('Alarm set for', time.asctime(time.localtime(set_time))) # print out a message indicating the alarm time
    myscheduler.run() # run scheduled events

if __name__ == "__main__":
    set_alarm(time.time()+1, os.path.join(os.getcwd(), "alarm.wav"), 'Wake up!')