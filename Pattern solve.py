# Pinned by CodeWithHarry
# WP WEB AGENCY
# 2 years ago (edited)
# Yasir Mehmood
import ctypes
import subprocess
import time
import webbrowser

import psutil
from plyer import notification

print("How Many Row You Want To Print")
one = int(input())
print("Type 1 Or 0")
two = int(input())
new = bool(two)
if new:
    for i in range(1, one + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
elif not new:
    for i in range(one, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

if new:
    for i in range(1, one + 1):
        for j in range(1, i + 1):
            print("#", end="")
        print()
elif not new:
    for i in range(one, 0, -1):
        for j in range(1, i + 1):
            print("#", end=" ")

# change theme
# ctypes.windll.user32.SystemParametersInfoW(20,
#                                            0,
#                                            "Location of wallpaper",
#                                            0)

# lock screens
# ctypes.windll.user32.LockWorkStation()

# shut down the pc
# subprocess.call('shutdown / p /f')

# to restart the pc
# subprocess.call(["shutdown", "/r"])

# find location of
# location = "pune"
# webbrowser.open("https://www.google.nl / maps / place/{0}".format(location))


while True:
    battery = psutil.sensors_battery()
    percent = battery.percent

    notification.notify(
        title="Battery Percentage",
        message=str(percent) + "% Battery remaining",
        timeout=10
    )

    # after every 60 mins it will show the
    # battery percentage
    time.sleep(60 * 60)
    continue
