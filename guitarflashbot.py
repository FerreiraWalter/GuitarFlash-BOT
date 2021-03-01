from PIL import ImageGrab
import pyautogui
import time

#FUNCTIONS
def capture_screen(): #FUNCIONANDO
    screen = ImageGrab.grab()
    return screen

#GREEN
def detected_green(screen): #FUNCIONANDO
    color = screen.getpixel((787, 783))
    if color == (0, 152, 0) or color == (255, 255, 255) or color == (1, 1, 1):
        return True

def press_green():
    pyautogui.press("A");

#RED
def detected_red(screen):
    color = screen.getpixel((878, 783))
    if color == (255, 0, 0) or color == (255, 255, 255) or color == (1, 1, 1):
        return True

def press_red():
    pyautogui.press("S");

#YELLOW
def detected_yellow(screen):
    color = screen.getpixel((969, 783))
    if color == (244, 244, 2) or color == (255, 255, 255) or color == (1, 1, 1):
        return True

def press_yellow():
    pyautogui.press("J");

#BLUE
def detected_blue(screen):
    color = screen.getpixel((1065, 783))
    if color == (0, 152, 255) or color == (255, 255, 255) or color == (1, 1, 1):
        return True

def press_blue():
    pyautogui.press("K");

#ORANGE
def detected_orange(screen):
    color = screen.getpixel((1143, 757))
    if color == (255, 101, 0) or color == (255, 255, 255) or color == (1, 1, 1):
        return True

def press_orange():
    pyautogui.press("L");

#MAIN PROGRAM
print('Starting in 2 seconds...')
time.sleep(2)

while True:
    screen = capture_screen();
    if detected_green(screen):
        press_green()
    if detected_red(screen):
        press_red()
    if detected_yellow(screen):
        press_yellow()
    if detected_blue(screen):
        press_blue()
    if detected_orange(screen):
        press_orange()
