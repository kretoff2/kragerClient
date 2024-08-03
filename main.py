import json
import time
import requests
import os.path
import flet as ft
from pages.mobile import sign_up_and_log_in

config = None
with open('config.json', 'r') as f:
    config = json.load(f)

dataStart = {
    "page":"messanger",
    "staticKey":"kaka",
    "deviceID":None,
    "account":{
        "active": False,
        "password": None,
        "name":None,
        "tag":None,
        "email":None,
        "number":None,
        "id":None,
        "conf":{
            "blackList":{},
            "ViewNumber":True,
            "ViewTime":True,
            "ViewEmail":False,
            "ViewIcon":True,
            "resandMessage":True,
            "collin":True,
            "gs":True,
            "sendMessage":True,
            "ViewdateOfBirthday":True,
            "ViewSubtitle":True
        }
    }
}
userData:json
if not os.path.exists('./data.json'):
    with open('data.json', 'w') as f:
        json.dump(dataStart, f)
with open('data.json', 'r') as f:
    userData = json.load(f)
def save_data():
    with open('data.json', 'w') as f:
        json.dump(userData, f)

def main(page:ft.Page):

    page.title = "krager"
    page.favicon = "assets/kragerLogo.jpg"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 600
    page.window_height = 1000
    page.window_resizable = False

    now_page = sign_up_and_log_in
    now_page.page = page
    now_page.userData = userData
    page.clean()
    page.add(now_page.pageUI)
    if now_page.enable_nav_bar == True:
        page.navigation_bar = now_page.nav_bar
    page.update()
ft.app(target=main, assets_dir="assets")