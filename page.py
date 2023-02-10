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
        self.element = self.drv
        for obj in self.object:
            print(obj)
            if 'many' in obj and obj['many']:
                self.find_elems(obj['by'], obj['attr'])
            else:
                self.find_elem(obj['by'], obj['attr'])

    def start(self, _action):
        actions = self.ACTIONS[_action]
        for action in actions:
            self.action = action
            self.object = self.OBJECTS[action["obj"]]
            self.element = self.ELEMENTS[action['obj']]
            self.data = action["data"] if "data" in action else ""
            command = action['cmd']
            print("CMD", command)
            eval("self." + command + "()")
            self.get_all_elements()



if __name__ == '__main__':
    page = Page(main)
    page.start("input_search_data")
    #page.start("click_sign_in")
    while True:
        pass
