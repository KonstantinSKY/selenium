#!/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.chrome.options import Options
from config import *


class Page:

    def __init__(self, name, drv):
        self.drv = drv
        self.__reload(name)
        # self.name = name
        # self.url = URLS[name]
        self.obj = [["tag name", "body"]]
        self.elem = self.drv.find_elements("tag name", "body")
        # self.acts = ""
        # self.objects = OBJECTS[name]
        # self.actions = ACTIONS[name]

    def __reload(self, name):
        self.name = name
        self.url = URLS[name]
        self.acts = ""
        self.objects = OBJECTS[name]
        self.actions = ACTIONS[name]
        #TODO get all content



    def find(self, obj: list):
        cur = self.drv
        for cmd in obj:
            print(cmd)
            if cmd[2]:  #TODO TRY decorator
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
        actions.click(self.elem)
        actions.perform()
        sleep(2)
        print("Clicked")


    def send_key_chain(self):
        actions = ActionChains(driver)
        actions.move_to_element(self.elem)
        actions.pause(0.5)  # TODO Random
        actions.click(self.elem)
        print("self.acts", self.acts)
        actions.send_keys(self.acts["data"])
        actions.perform()
        sleep(2)
        print("Sent key")


    def click(self, obj=None):
        print(obj)
        self.obj = obj if obj is not None else self.obj
        print(obj)
        self.find(obj)
        self.click_chain()
        #TODO Reload if sign_in
    def send_key(self, obj):
        print(obj)
        self.obj = obj if obj is not None else self.obj
        print(obj)
        self.find(obj)
        self.send_key_chain()

    def start(self, acts):
        for action in self.actions[acts]:
            print("ACTION", action)
            if action["cmd"] == "click":
                self.click(action["obj"])
            if action["cmd"] == "send_keys":
                print("action", action)
                self.acts = action
                self.send_key(action["obj"])
            sleep(5)



if __name__ == '__main__':
    opts = Options()
    opts.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=opts)  # Optional argument, if not specified will search path.
    driver.get('https://www.google.com/')
    #driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    #sleep(100)
    # driver.find_element()
    page = Page("main", driver)
    page.start("click_sign_in")
    page.start("insert_email_login")
    # page.drv.find_element("tag name", "a")
    #page.sign_button = [["xpath", '//*[@id="gb"]/div/div[2]/a', False], ]
    #page.click(page.sign_button)
    #print(page.drv.current_url)
    while True:
        pass
