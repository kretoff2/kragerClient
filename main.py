import json
import os.path
import flet as ft

from pages import open_page, data

config = None
with open('config.json', 'r') as f:
    config = json.load(f)

dataStart = {
    "page":"sign_up_and_log_in",
    "color_theme":"#3f008d",
    "standart_text_size_h1":50,
    "standart_text_size_h2":45,
    "standart_text_size_h3":35,
    "standart_text_size_h4":25,
    "standart_text_size_h5":20,
    "standart_text_size_h6":15,
    "standart_text_size_l":8,
    "veiw_text_size":25,
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

data.userData = userData

from pages.mobile import sign_up_and_log_in, messanger, global_settings, menu

def main(page:ft.Page):
    page.title = "krager"
    page.theme_mode = 'dark'
    path = os.path.abspath("./assets/icon.ico")
    page.window_icon = path
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 600
    page.window_height = 1000
    page.window_resizable = True
    page.scroll = ft.ScrollMode.AUTO

    page.theme = ft.Theme(color_scheme_seed=userData["color_theme"])

    if userData['account']['active'] == False:
        page.theme = ft.Theme(color_scheme_seed="deep purple")
        open_page.open_page(sign_up_and_log_in, page, userData)
    else: exec(f"open_page.open_page({userData['page']}, page, userData)")

ft.app(target=main, assets_dir="assets")