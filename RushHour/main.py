# coding=utf-8
import os
import time
from ocr import recognize
from selenium import webdriver

import uiautomator2 as u2

d = u2.connect_usb()

origin_dir = 'img/'
if not os.path.isdir(origin_dir):
    os.mkdir(origin_dir)

img_ext = ''


def pull_screenshot(mission):
    img_path = '/sdcard/DCIM/{}{}.png'.format(img_ext, mission)
    os.system('adb shell screencap -p {}'.format(img_path))
    os.system('adb pull {} {}'.format(img_path, origin_dir))


if __name__ == '__main__':
    browser = webdriver.Firefox()
    url = "http://www.baidu.com"
    browser.get(url)
    i = 0
    while True:
        flag = raw_input("come on~\n")
        start = time.time()
        last_point = time.time()
        print "get~", flag
        i = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # pull_screenshot(i)
        #
        # now = time.time()
        # print "get screenshot", now - last_point
        # last_point = now
        #
        # im = Image.open("{}{}{}.png".format(origin_dir, img_ext, i))

        im = d.screenshot()
        now = time.time()
        print "d.screenshot", now - last_point
        last_point = now

        res = recognize(im)
        print res

        now = time.time()
        print "recognize", now - last_point
        last_point = now

        url = "http://www.baidu.com/s?ie=UTF-8&wd=%s" % res
        browser.get(url)

        now = time.time()
        print "brower", now - last_point
        last_point = now
        print "total", now - start
        im.save("{}{}{}.png".format(origin_dir, img_ext, i))
    browser.quit()
