import mouse
import keyboard
import time
while True:
  if keyboard.is_pressed("ctrl+space"):
    break
  else:
    mouse.click('left')
    time.sleep(
