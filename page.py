#!/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class Page:

    def __init__(self, drv):
        self.drv = drv
        self.elem = ""
        self.obj = ""

    def find(self, obj: list):
        cur = self.drv
        for cmd in obj:
            print(cmd)
            if cmd[2]:
                cur = cur.find_elements(cmd[0], cmd[1])
            else:
                cur = cur.find_element(cmd[0], cmd[1])
        print(cur)
        self.elem = cur
        return cur

    def click_chain(self):
        actions = ActionChains(driver)
        actions.move_to_element(self.elem)
        actions.pause(0.5)  # TODO Random
        # actions.context_click()
        # actions.pause(5)
        # actions.send_keys("escape")
        actions.click(self.elem)
        actions.perform()
        sleep(2)
        print("Clicked")

    def click(self, obj=None):
        print(obj)
        self.obj = obj if obj is not None else self.obj
        
        self.find(obj)
        self.click_chain()


if __name__ == '__main__':
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://www.google.com/')
    # driver.find_element()
    page = Page(driver)
    # page.drv.find_element("tag name", "a")
    page.sign_button = [["xpath", '//*[@id="gb"]/div/div[2]/a', False], ]
    page.click(page.sign_button)
    while True:
        pass
