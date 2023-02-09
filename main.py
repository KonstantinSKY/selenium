from typing import Dict, List, Any

from page import *


def get_config():
    pass



class Login(Page):


    def __init__(self, drv):
        super().__init__(drv)
        #self.email_input =
        #self.next_button =
        self.name =""
        self.url = ""
        self.objects = {
            "sb": [[]],
            "obj2":[[]],
        }
        self.actions = {
            "click_sign_in": [{"cmd":"click", "obj": self.objects["sb"], "data":"", "link":" "},]

        }


    def open(self):
        # for page in config:
        #  "   if self.config  = self.drv.current_url"
            # pass

    def login(self):
        pass


if __name__ == '__main__':
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://www.google.com/')
    login_page = Login(driver)
    print(login_page.__dir__())

    while True:
        pass
