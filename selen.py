#!/bin/python

# Modern selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.chrome.options import Options


class Selen:

    def __init__(self):
        opts = Options()
        opts.add_argument('--disable-blink-features=AutomationControlled')
        self.drv = webdriver.Chrome(options=opts)

    def check_webdriver_data(self):
        print("Checking webdriver ...")
        self.drv.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
        anykey = input("Any key for close webdriver and reinit instance")
        self.drv.quit()
        self.__init__()


if __name__ == '__main__':
    sel_inst = Selen()
    #sel_inst.check_webdriver_data()
    sel_inst.drv.get('https://qasvus.wixsite.com/ca-marketing')
    while True:
        pass