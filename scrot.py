#!/usr/bin/env python
# Named for the Linux SCReenshOT command for screen capture, this script captures
# a screenshot and saves it with a timestamp-based filename as a PNG file. 
from PIL import Image
import datetime
import pyautogui
import sys

timestamp = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
print(timestamp)
fname = 'screen' + timestamp + '.png'
screenshot = pyautogui.screenshot()
screenshot.save(fname)

im = Image.open(fname)
im.show()
