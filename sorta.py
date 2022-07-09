import psutil
import winsound
import time
battery = psutil.sensors_battery()
plugged = battery.power_plugged
#percent = str(battery.percent)
x = int(battery.percent)
if plugged == False:
    plugged = "Not Plugged In"
else:
    plugged="Plugged In"
print(x,'% | '+plugged)
if(x==100):
    winsound.PlaySound('sound.wav',winsound.SND_FILENAME)


