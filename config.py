from typing import Dict, List, Any

from page import *

# Page names
main = "main"
sign_in = "sign_in"


# pages configs
URLS = {main: "https://www.google.com/",
        sign_in: "https://accounts.google.com/v3/signin/"



         }

OBJECTS = {
    main: {
        "sign_in_button": [['xpath', '//*[@id="gb"]/div/div[2]/a', False]],
        "email_login_field": [['id', 'identifierId', False]],
        "next_button": [['id', 'identifierNext', False]],
    },
    sign_in: {
        "email_login_field": [['id', 'identifierId', False]],
        "next_button": [['id', 'identifierNext', False]],
    }
}


ACTIONS = {
    main: {
        "click_sign_in": [{"cmd": "click", "obj": OBJECTS[main]["sign_in_button"], "data": "", "link": sign_in},],
        "insert_email_login": [
            {"cmd": "send_keys", "obj": OBJECTS[main]["email_login_field"], "data": "stan.sky@gmail.com"},
            {"cmd": "click", "obj": OBJECTS[main]["next_button"], "link": sign_in},
        ],
    },
    sign_in: {
        "insert_email_login": [
            {"cmd": "send_keys", "obj": OBJECTS[main]["email_login_field"], "data": "my_email@gmail.com", "link": " "},],
    },
}
