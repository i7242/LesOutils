#! python3
import pyautogui

# use "position()" to get the position x,y
#   0. This is to get the position of buttons.
#        need to be done before run the scrip.
#        need to be customized.
#   1. first open python in powershell
#   2. input the command below
#   3. move pointer to the button position
#   4. press "Enter" to run the command below
#   5. read x, y, fill them to the processes below
#
#   x,y = pyautogui.position()

# 1 "Proceed to Step 2 of 3"
x1 = 521
y1 = 718

# 2 "Finish Enrolling"
x2 = 739
y2 = 504

# 3 "Add Another Class"
x3 = 485
y3 = 506

pyautogui.PAUSE = 10

pyautogui.moveTo(x1,y1,duration=1)


pyautogui.PAUSE = 10

# Here set it never stops
#   1. if one clase has enrolled, the button position will change
#       the predefined process doesnót work
#   2. to force stop, move the pointer quickly to the left-up corner
#       of the screen, for several seconds
while True:
    pyautogui.click(x1,y1,button='left')
    
    pyautogui.click(x2,y2,button='left')
    
    pyautogui.click(x3,y3,button='left')


