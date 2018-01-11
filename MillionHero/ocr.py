# coding=utf-8
import pytesseract
import time
from PIL import Image
from selenium import webdriver

import sys

sys.path.append('..')
from utils import reformat

WHITE_BACKGROUND_COLOR = (255, 255, 255)
RED_COLOR = (252, 49, 108)


def write_line(im, y=0):
    w, h = im.size
    for x in xrange(0, w):
        im.putpixel((x, y), RED_COLOR)


def get_change_point_y(im):
    data = im.getdata()

    # im = Image.open('big-2lines.jpeg')

    width, height = im.size

    pre_pix = None
    change_point_y = []

    # for y in xrange(int(0.13 * height), height, 4):
    for y in xrange(int(0.13 * height), height, 15):
        cur_pix = data[width * y + int(0.5 * width)]
        if cur_pix == WHITE_BACKGROUND_COLOR and pre_pix == WHITE_BACKGROUND_COLOR:
            change_point_y.append(y)
        pre_pix = cur_pix
    #
    # for y in change_point_y:
    #     write_line(im, y=y)
    #
    # im.show()
    return change_point_y


def recognize(im):
    width, height = im.size
    change_point_y = get_change_point_y(im)
    if len(change_point_y) < 1:
        bottom = height
    else:
        bottom = change_point_y[-1]

    t_im = im.crop((0.05 * width, 0.18 * height, 0.95 * width, bottom))  # x0, y0, x1, y1
    # t_im.show()
    t_str = pytesseract.image_to_string(t_im, lang="chi_sim", config="-psm 6")

    t_str = reformat(t_str)

    if t_str.count("\n") > 3:
        t_str = t_str.replace("\n", "", 1).replace("\n", " ")
    else:
        t_str = t_str.replace("\n", " ")

    print "recognize", t_str
    return t_str


if __name__ == '__main__':
    im = Image.open('img/2018-01-10 20:14:11.png')
    im.show()

    last_point = time.time()
    res = recognize(im)
    now = time.time()
    print "recognize", now - last_point
    last_point = now
    #
    browser = webdriver.Firefox()
    url = "https://www.baidu.com/s?ie=UTF-8&wd=%s" % res
    browser.get(url)
