#!/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.chrome.options import Options
from config import *
from selen import Selen


class Page(Selen):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.url = name[URL]
        self.drv.get(self.url)
        self.obj = [["tag name", "body"]]
        self.acts = ""
        self.OBJECTS = name[OBJECTS]
        self.ACTIONS = name[ACTIONS]
        self.ELEMENTS = {}
        self.drv.get(self.url)
        self.get_all_elements()

    def __reload(self, name):
        self.name = name
        self.url = URLS[name]
        self.acts = ""
        self.objects = OBJECTS[name]
        self.actions = ACTIONS[name]
        #TODO get all content

    def get_all_elements(self):
        for name, obj in self.OBJECTS.items():
            self.object = obj
            self.find()
            if "_id" not in vars(self.element).keys():
                continue
            self.ELEMENTS[name] = self.element

        print("ELEMENTS", self.ELEMENTS)

    def find(self):
        self.print_arg()
        self.element = self.drv
        for cmd in self.object:
            print(cmd)
            if cmd[2]:
                self.find_elems(cmd[0], cmd[1])
            else:
                self.find_elem(cmd[0], cmd[1])

    def click_chain(self):
        actions = ActionChains(self.drv)
        self.act_chain.move_to_element(self.elem)
        self.act_chain.pause(0.5)  # TODO Random
        eval("self.act_chain.click(self.elem)")
        self.act_chain.perform()
        sleep(2)
        print("Clicked")


    def send_key_chain(self):
        #actions = ActionChains(self.drv)
        self.act_chain.move_to_element(self.elem)
        self.act_chain.pause(0.5)  # TODO Random
        self.act_chain.click(self.elem)
        print("self.acts", self.acts)
        self.act_chain.send_keys(self.acts["data"])
        self.act_chain.perform()
        sleep(2)
        print("Sent key")



    def click(self):
        self.find()
        self.click_chain()
        #TODO Reload if sign_in
    def send_key(self, obj):
        print(obj)
        self.obj = obj if obj is not None else self.obj
        print(obj)
        self.find(obj)
        self.send_key_chain()

    def start(self, _action):
        actions = self.actions[_action]
        for action in actions:
            self.actions = action
            self.object = action["obj"]
            command = action['cmd']
            print("CMD", command)
            eval("self." + command)


            print("ACTION", action)
            if action["cmd"] == "click":
                self.object = action["obj"]
                self.click()

            if action["cmd"] == "send_keys":
                print("action", action)
                self.acts = action
                self.send_key(action["obj"])
            sleep(5)



if __name__ == '__main__':
    page = Page(main)


    # "opts = Options()
    # "opts.add_argument('--disable-blink-features=AutomationControlled')
    # "driver = webdriver.Chrome(options=opts)  # Optional argument, if not specified will search path.
    # "driver.get('https://www.google.com/')
    #driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    #sleep(100)
    # driver.find_element()
    # page.start("click_sign_in")
    # page.start("insert_email_login")
    # page.drv.find_element("tag name", "a")
    #page.sign_button = [["xpath", '//*[@id="gb"]/div/div[2]/a', False], ]
    #page.click(page.sign_button)
    #print(page.drv.current_url)
    while True:
        pass
