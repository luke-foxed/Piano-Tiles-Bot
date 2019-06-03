import os
import sys
import time
import webbrowser

import pyautogui
from pynput.mouse import Button, Controller
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from PIL import Image

browser = webdriver.Chrome(ChromeDriverManager().install())

pyautogui.FAILSAFE = True
game_mode = ' '.join(sys.argv[1:])
pyautogui.PAUSE = 0


def main():
    browser.get('http://tanksw.com/piano-tiles/')
    browser.maximize_window()
    select_mode(game_mode)

    start = time.time()

    while 0 < 1:
        black_tile = get_black_tile()


def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None
    pixel = image.getpixel((i, j))
    return pixel


def select_mode(game_mode):
    if game_mode == 'classic':
        classic_mode = browser.find_element_by_xpath("//*[@id='menu']/div[1]").click()

    if game_mode == 'arcade':
        arcade_mode = browser.find_element_by_xpath("//*[@id='menu']/div[2]").click()


def get_black_tile():
    i = 0
    x = 44
    y = 400
    black_pixel = []

    region_image = pyautogui.screenshot(region=(750, 280, 400, 600))
    for i in range(4):
        pixel = get_pixel(region_image, x, y)
        next_pixel = get_pixel(region_image, x, y - 10)
        if pixel == (19, 19, 19):
            if next_pixel == (19, 19, 19):
                black_pixel = [x+750, y +280]
                play_game(black_pixel)
        else:
            x = x + 100


def play_game(black_pixel):
    x = int(black_pixel[0])
    y = int(black_pixel[1])
    pyautogui.moveTo(x, y+100)
    pyautogui.click(x, y + 48)


if __name__ == "__main__":
    main()
