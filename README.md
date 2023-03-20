# Minecraft Skyblock AFK Bypass Script

This Python script is designed for Minecraft server skyblock players to prevent getting kicked by an antiafk plugin. The script simulates user activity on a Windows machine using keystrokes and mouse clicks. The delay between the simulated user activity and the call to the afk() function can be adjusted by modifying the value passed to the time.sleep() function. By default, the delay is set to 270 seconds (4.5 minutes), but this value can be increased or decreased to suit the user's needs.

## Installation

1. Install Python 3.x on your Windows machine.
2. Run CMD as administrator.
3. Install the pywin32 and pyautogui libraries using pip. 
```
pip install pywin32 pyautogui
```
4. Clone or download the script to your local machine.

## Usage

1. Run the script using Python 3.x.
```
python afk.py
```
3. Immediately go back to your Minecraft window and set your crosshair at stone generator.
2. The script will start simulating user activity on your machine.
3. To stop the script, press Ctrl+C or close the command prompt window.

PS: If the script interrupts any of your computer's actions, you can start spamming the right mouse click on the command prompt window to regain control.

## Customization

The delay between the simulated user activity and the call to the afk() function can be adjusted by modifying the value passed to the time.sleep() function. Be sure to test the delay to ensure it is working as intended and not causing issues with the server or being flagged as a bot.

```python
def main():
    time.sleep(5) # Delay in seconds between starting the script and getting back to minecraft window
    while True:
        pyautogui.mouseDown()

        time.sleep(270) # Delay in seconds between simulating activity (default: 4 min 30 sec)
        afk()
```

## Caution

While this script is useful for preventing being kicked from the server due to inactivity, it should be used with caution. Ensure that it is not running unnecessarily, as it may consume system resources and interfere with other running applications. Additionally, the script may not work with certain anti-cheat plugins or servers that have strict anti-bot policies. Use at your own risk.
