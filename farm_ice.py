import pkg_resources
import pyautogui as auto
from python_imagesearch.imagesearch import imagesearch as search
import time
from printy import printy
import sys
import pyautogui

pkg_resources.require("PyAutoGUI==0.9.50")
pkg_resources.require("opencv-python==4.5.1.48")
pkg_resources.require("python-imageseach-drov0==1.0.6")

auto.FAILSAFE = False

# Start utility methods
def onscreen(path, precision=0.8):
    return search(path, precision)[0] != -1

def search_to(path):
    pos = search(path)
    if onscreen(path):
        auto.moveTo(pos)
        return pos

def click_key(key, delay=.1):
    auto.keyDown(key)
    time.sleep(delay)
    auto.keyUp(key)

def click_left(delay=.1):
    auto.mouseDown()
    time.sleep(delay)
    auto.mouseUp()

def click_to(path, delay=.1):
    if onscreen(path):
        auto.moveTo(search(path))
        click_left(delay)

def hold_key(key, holdtime):
    pyautogui.keyDown(key)
    time.sleep(holdtime)
    pyautogui.keyUp(key)
# End utility methods

global game_count, debug
game_count = 0
debug = False

def enter_battle():
    global game_count
    while onscreen("./screenshots/pet.png"):
        auto.moveTo(200, 200)
        click_left()
        hold_key('w', 1)
        hold_key('s', 1)
    if debug:
        print("[DEBUG] Entering battle!")
    print(f'Total Battles Finished: {game_count}')
    game_count += 1
    loading()

def loading():
    while not onscreen("./screenshots/pass.png"):
        time.sleep(1)
    if debug:
        print("[DEBUG] In battle!")
    in_battle()
    
def in_battle():
    while not onscreen("./screenshots/pet.png"):
        choose_card()
        time.sleep(0.5)
    enter_battle()

def choose_card():
    while onscreen("./screenshots/pass.png"):
        click_to("./screenshots/wyvern.png")
        if debug:
            print("[DEBUG] Casting spell!")
        time.sleep(0.5)

if __name__ == "__main__":
    if sys.argv[1] == "-d":
        debug = True

enter_battle()


