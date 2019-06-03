
import sys
import time
import pyautogui
from PIL import Image
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
pyautogui.FAILSAFE = True
game_mode = ' '.join(sys.argv[1:])
pyautogui.PAUSE = 0

start_x = 750
stary_y = 690

bottom_row = (start_x, stary_y, start_x + 400, 1)
middle_row = (start_x, stary_y - 150, start_x + 400, stary_y + 1)
top_row = (start_x, stary_y - 300, start_x + 400, stary_y + 1)

black = (19, 19, 19)
red = (248, 52, 56)
grey = (157, 157, 157)

score = 0
y_adjustment = 30
previous_lane = 0


def main():
    select_mode(game_mode)
    time.sleep(3)
    click_bottom_tiles() # start the game
    while 0<1:
        click_middle_tiles()


def select_mode(game_mode):
    browser.get('http://tanksw.com/piano-tiles/')
    browser.maximize_window()
    if game_mode == 'classic':
        classic_mode = browser.find_element_by_xpath("//*[@id='menu']/div[1]").click()

    if game_mode == 'arcade':
        arcade_mode = browser.find_element_by_xpath("//*[@id='menu']/div[2]").click()


def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None
    pixel = image.getpixel((i, j))
    return pixel


def click_bottom_tiles():
    global y_adjustment, black, red, previous_lane
    starting_pos = 50
    bottom_image = pyautogui.screenshot(region=bottom_row)
    for i in range(4):
        # to-do --> count how many times code is looped here and devide score by that amount each time
        pixel = get_pixel(bottom_image, starting_pos, 0)
        if pixel == black:
            click(start_x + starting_pos, stary_y + y_adjustment)
            break
        elif pixel == red or pixel == grey:
            print('YOUR SCORE ', score)
            sys.exit()
        else:
            starting_pos = starting_pos + 100  # move to next tile


def click_middle_tiles():
    global y_adjustment, black, red, previous_lane
    starting_pos = 50
    middle_image = pyautogui.screenshot(region=middle_row)
    for i in range(4):
        pixel = get_pixel(middle_image, starting_pos, 0)
        if pixel == (19, 19, 19):
            click(start_x + starting_pos, (stary_y-150) + y_adjustment)
            print('clicking ', (stary_y-150) + y_adjustment)
            break
        elif pixel == red or pixel == grey:
            print('YOUR SCORE ', round(score/3))
            sys.exit()
        else:
            starting_pos = starting_pos + 100  # move to next tile

# def click_bottom_tiles():
#     global y_adjustment, black, red, current_pixel
#     starting_pos = 50
#     bottom_image = pyautogui.screenshot(region=bottom_row)
#
#     pixel1 = get_pixel(bottom_image, starting_pos, 0)
#     pixel2 = get_pixel(bottom_image, starting_pos+100, 0)
#     pixel3 = get_pixel(bottom_image, starting_pos+200, 0)
#     pixel4 = get_pixel(bottom_image, starting_pos+300, 0)
#
#     if pixel1 == black:
#         pyautogui.moveTo(start_x + starting_pos, stary_y + y_adjustment)
#         if pyautogui.position() == current_lane:
#             print('CURRENT LANE: ', current_lane)
#             print('MOUSE: ' , pyautogui.position())
#             pass
#         else:
#             click(start_x + starting_pos, stary_y + y_adjustment)
#     elif pixel2 == black:
#         pyautogui.moveTo(start_x + starting_pos+100, stary_y + y_adjustment)
#         if pyautogui.position() == current_lane:
#             print('CURRENT LANE: ', current_lane)
#             print('MOUSE: ' , pyautogui.position())
#             pass
#         else:
#             click(start_x + starting_pos+100, stary_y + y_adjustment)
#     elif pixel3 == black:
#         pyautogui.moveTo(start_x + starting_pos+200, stary_y + y_adjustment)
#         if pyautogui.position() == current_lane:
#             print('CURRENT LANE: ', current_lane)
#             print('MOUSE: ' , pyautogui.position())
#             pass
#         else:
#             click(start_x + starting_pos+200, stary_y + y_adjustment)
#     elif pixel4 == black:
#         pyautogui.moveTo(start_x + starting_pos+300, stary_y + y_adjustment)
#         if pyautogui.position() == current_lane:
#             print('CURRENT LANE: ', current_lane)
#             print('MOUSE: ' , pyautogui.position())
#             pass
#         else:
#             click(start_x + starting_pos+300, stary_y + y_adjustment)



def click(x, y):
    global score
    pyautogui.click(x, y)
    score += 1
    click_adjustment(score)

#
#
# def click_top_tiles():
#     starting_pos = 50
#     top_image = pyautogui.screenshot(region=top_row)
#     for i in range(4):
#         pixel = get_pixel(top_image, starting_pos, 0)
#         if pixel == (19, 19, 19):
#             pyautogui.moveTo(start_x + starting_pos, stary_y + 760)
#             pyautogui.click(start_x + starting_pos, stary_y - 270, clicks=1)
#             break
#         else:
#             starting_pos = starting_pos + 100  # move to next tile
#     click_middle_tiles()

def click_adjustment(score):
    global y_adjustment
    if round(score/3) == 100:
        y_adjustment += 11

    if round(score/3) == 200:
        y_adjustment += 22

    if round(score/3) == 400:
        y_adjustment += 33

    if round(score/3) == 800:
        y_adjustment += 44

    if round(score/3) == 1600:
        y_adjustment += 55
        
    return y_adjustment


if __name__ == "__main__":
    main()
