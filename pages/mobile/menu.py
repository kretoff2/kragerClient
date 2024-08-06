import flet as ft
import json
import time

import pages.mobile.overlay_menu
from pages import open_page, data
import requests

SERVER_IP = "localhost"
SERVER_PORT = 80

page:ft.Page
enable_nav_bar = False
userData = data.userData

pageUI = None

def open_app(e):
    open_page.open_page(e.control.data, page, userData)
def init():
    global pageUI
    page.bgcolor = ft.colors.ON_PRIMARY_CONTAINER
    messanger = ft.Container(content=ft.Row([ft.Image(width=100, height=100), ft.Text("Чаты", size=35, color=ft.colors.ON_PRIMARY)]), margin=ft.margin.symmetric(vertical=5, horizontal=5))
    apps = [messanger]
    pageUI = ft.Column(apps)
