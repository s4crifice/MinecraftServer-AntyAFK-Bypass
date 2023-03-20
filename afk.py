#!/usr/bin/env python3

import time
import win32api
import win32con
import pyautogui

def afk():
    win32api.keybd_event(0x53, 0, 0, 0) # "S" - move backward
    time.sleep(0.5)
    win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(0x57, 0, 0, 0) # "W" - move forward
    time.sleep(0.5)
    win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)
    return

# VVV README.md
def main():
    time.sleep(5)
    while True:
        pyautogui.mouseDown()

        time.sleep(270)
        afk()
        

if __name__ == '__main__':
    main()
