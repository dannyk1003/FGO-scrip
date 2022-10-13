import pyautogui

# pyautogui.moveTo(484, 130, duration = 1.5) # move to (100, 100)

pyautogui.dragTo(973, 130, duration=2, button='left')

print(pyautogui.position())
print(pyautogui.size())

x, y = pyautogui.position()
rgb = pyautogui.screenshot().getpixel((x, y))


print(rgb)

myScreenshot = pyautogui.screenshot()
myScreenshot.save('MyScreenShot.png')