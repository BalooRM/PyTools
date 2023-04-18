#!/usr/bin/env python
# Named for the Linux SCReenshOT command for screen capture, this script captures
# a screenshot and saves it with a timestamp-based filename as a PNG file. 
from PIL import Image
import datetime
import pyautogui
import sys

# get app name to find its window
app = sys.argv[0]
if 'C:' in app:     # when invoked with #! (without python) grab from full path
    app = sys.argv[0].split('\\')[-1]
window = ''   # save window and position
left = 0
top = 0
windows = pyautogui.getAllWindows()
for w in windows:
    wt = w.title
#    if (('Windows' in wt) and (app in wt)):
    if ((app in wt)):        
        window = w
        left = int(w.left)
        top = int(w.top)
        #print('left,top=', ','.join([str(left), str(top)]))

timestamp = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
print(timestamp)
fname = 'screen' + timestamp + '.png'
screenshot = pyautogui.screenshot()
screenshot.save(fname)

im = Image.open(fname)
im.show()
print(fname)
if window != '':     # if window found, click it to return focus
    pyautogui.click(left+50, top+50)
else:
    print(app, 'window not found')
