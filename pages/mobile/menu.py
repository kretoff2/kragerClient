import flet as ft
import json
import time

import pages.mobile.overlay_menu
from pages import open_page, data
from pages.mobile import messanger, global_settings
import requests
name = "menu"

SERVER_IP = "localhost"
SERVER_PORT = 80

page:ft.Page
enable_nav_bar = False
userData = data.userData

pageUI = None

def open_app(e):
    open_page.open_page_with_name(e.control.data, page, userData)
def init():
    global pageUI
    page.bgcolor = ft.colors.BACKGROUND
    messanger = ft.Container(content=ft.Row([ft.Icon(ft.icons.MESSAGE, size=userData["standart_text_size_h2"], color=ft.colors.PRIMARY), ft.Text("Чаты", size=userData["standart_text_size_h3"], color=ft.colors.PRIMARY)]), margin=ft.margin.symmetric(vertical=5, horizontal=5), bgcolor=ft.colors.PRIMARY_CONTAINER,padding=ft.padding.symmetric(horizontal=10), data="messanger", on_click=open_app)
    apps = [messanger]
    pageUI = ft.Column(apps)
