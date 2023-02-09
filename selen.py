#!/bin/python

# Modern selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.chrome.options import Options


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except NoSuchElementException:
            print(f"In {func.__name__} was  Error")
            return None
    return inner_function


class Selen:

    def __init__(self):
        opts = Options()
        opts.add_argument('--disable-blink-features=AutomationControlled')
        self.drv = webdriver.Chrome(options=opts)
        self.element = self.drv
        self.object = [[]]
        self.action = ""
        self.data = ""
        self.act_chain = ActionChains(self.drv)

    def check_webdriver_data(self):
        print("Checking webdriver ...")
        self.drv.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
        anykey = input("Any key for close webdriver and reinit instance")
        self.drv.quit()
        self.__init__()

    def get(self, url):
        self.drv.get(url)

    @exception_handler
    def find_elem(self, by, content):
        self.element = self.element.find_element(by, content)

    @exception_handler
    def find_elems(self, by, content):
        self.element = self.element.find_elements(by, content)

    def print_arg(self):
        print('self.elem :', self.element)
        print('self.obj :', self.object)
        print('self.action :', self.action)
        print('self.data :', self.data)

if __name__ == '__main__':
    sel_inst = Selen()
    # sel_inst.check_webdriver_data()
    sel_inst.drv.get('https://qasvus.wixsite.com/ca-marketing')
    while True:
        pass
