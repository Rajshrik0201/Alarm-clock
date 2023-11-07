import time
from playsound import playsound

def set_alarm(alarm_time,sound_file):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            playsound(sound_file)
            break
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time(HH:MM:SS): ")
    sound_file = "audio.mp3"
    set_alarm(alarm_time,sound_file)