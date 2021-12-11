import os, math, time
from pynput.keyboard import Key, Controller
import time
while True:
    time.sleep(3)

    def delay(limit):
        while limit > 0 :
            #print("%s seconds remaining" % (limit))
            limit = limit -1

    keyboard = Controller()
    #start

    keyboard.press(Key.cmd_l)
    keyboard.press("d")
    keyboard.release("d")
    keyboard.release(Key.cmd_l)

    # Key strokes


    key = "r"
    keyboard.press(Key.cmd_l)
    keyboard.press(key)
    keyboard.release(key)
    keyboard.release(Key.cmd_l)
    time.sleep(0.3)


    keystrokesCommand = "PowerShell.exe"

    for i in keystrokesCommand:
        keyboard.press(i)
        keyboard.release(i)

    

    #delay(50000)


    keyboard.press(Key. enter)
    keyboard.release(Key. enter)
    keyboard.press(Key. enter)
    keyboard.release(Key. enter)
    
    time.sleep(0.4)
    delay(5400)
    
    commands = "exit"
    
    
    for t in commands:
            keyboard.press(t)
            keyboard.release(t)
            
    keyboard.press(Key. enter)
    keyboard.release(Key. enter)
    
    time.sleep(0.4)
    #end

    keyboard.press(Key.cmd_l)
    keyboard.press("d")
    keyboard.release("d")
    keyboard.release(Key.cmd_l)
    
    keyboard.press(Key. alt)
    keyboard.press(Key. tab)
    keyboard.release(Key. tab)
    keyboard.release(Key. alt)


    # Commands :

    os.access("C:\\users\\Titanium2", 1)
    os.chdir("C:\\users\\Titanium2")
    #os.system("dir")
    #os.mkdir("SheeeeeSh")
    #os.system("code .")

    #input(">/")
    time.sleep(60)