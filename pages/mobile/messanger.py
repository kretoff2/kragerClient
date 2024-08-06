import flet as ft
import json
import time

import pages.mobile.overlay_menu
from pages import data
import requests

SERVER_IP = "localhost"
SERVER_PORT = 80

page:ft.Page
enable_nav_bar = False
userData = data.userData

pageUI = None

temp = {"chats":{}}
def overlay_menu(e):
    pages.mobile.overlay_menu.page = page
    pages.mobile.overlay_menu.overlay.visible = True
    pages.mobile.overlay_menu.userData = userData
    page.update()

header = ft.Container(
    content=ft.Row([ft.IconButton(ft.icons.MENU, icon_color=ft.colors.ON_PRIMARY, bgcolor=ft.colors.PRIMARY, icon_size=30, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE), on_click=overlay_menu),ft.Text("Krager", size=25, color=ft.colors.ON_PRIMARY)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,spacing=50)
)
def openChat(chatID):
    print(chatID)

MyChats = None
def on_chat_click(e):
    chatId = e.control.data
    openChat(chatId)

def chats():
    chats = []
    r = requests.get(f"http://{SERVER_IP}:{SERVER_PORT}/get_my_chats")
    data = r.json()
    for el in data["chatList"]:
        title = "None"
        if data["chatList"][el]["user1ID"] == userData["account"]["id"]:
            title = data["chatList"][el]["user2ID"]
        elif data["chatList"][el]["user2ID"] == userData["account"]["id"]:
            title = data["chatList"][el]["user1ID"]
        chats.append(ft.Container(content=ft.Container(content=ft.Row([ft.Column([ft.Text(title, size=25, color=ft.colors.PRIMARY_CONTAINER), ft.Text(data["chatList"][el]["lastMessage"], size=15, color=ft.colors.SECONDARY_CONTAINER)])]), margin=ft.margin.symmetric(horizontal=10, vertical=5)), bgcolor=ft.colors.PRIMARY, margin=ft.margin.all(1), data=el, on_click=on_chat_click))
    return chats
def init():
    global pageUI, MyChats
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.colors.BACKGROUND
    page.window_min_width = 400
    page.window_min_height = 200
    MyChats = chats()
    if MyChats != None:
        for el in MyChats:
            print(el)
    nnUI = ft.Column(
        [
            ft.Container(
                content=header,
                bgcolor=ft.colors.PRIMARY,
                margin=ft.margin.only(bottom=5, left=0, right=0, top=0),
                height=60,
            ),
            ft.Container(
                content=ft.Column(MyChats),
                margin=ft.margin.only(bottom=5, left=1, right=1, top=0),
                bgcolor=ft.colors.SECONDARY
            )

        ]
    )
    pages.mobile.overlay_menu.overlay.margin = ft.margin.only(right=page.window_width*0.3, bottom=page.window_height*0.1)
    pageUI = ft.Stack(
        controls=[
            nnUI,
            pages.mobile.overlay_menu.overlay
        ]
    )

