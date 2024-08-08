import flet as ft
import json
import time

import pages.mobile.overlay_menu
from pages import data
import requests

name = "messanger"

SERVER_IP = "localhost"
SERVER_PORT = 80

page:ft.Page
enable_nav_bar = False
userData = data.userData

pageUI = None

temp = {"chats":{}}

GLchatID = "kall"
nnn = False
def overlay_menu(e):
    pages.mobile.overlay_menu.page = page
    pages.mobile.overlay_menu.overlay.visible = True
    pages.mobile.overlay_menu.userData = userData
    page.update()
def search_btn(e):
    search_UI.visible = True
    page.update()

header = ft.Container(
    content=ft.Row([ft.IconButton(ft.icons.MENU, icon_color=ft.colors.PRIMARY, bgcolor=ft.colors.ON_PRIMARY, icon_size=userData["standart_text_size_h2"], animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE), on_click=overlay_menu),ft.Text("Krager", size=userData["standart_text_size_h4"], color=ft.colors.PRIMARY), ft.IconButton(icon=ft.icons.SEARCH, icon_size=userData["standart_text_size_h3"], icon_color=ft.colors.PRIMARY, on_click=search_btn)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,spacing=50)
)
def send_message(e):
    global GLchatID
    header = {"my_id": userData["account"]["id"], "deviceID": str(userData["deviceID"])}
    if nnn == False:
        data = {"chatID":GLchatID, "user2ID":None, "message":messageTextField.value}
    else:data = {"chatID":None, "user2ID":GLchatID, "message":messageTextField.value}
    dataJ = json.dumps(data)
    r = requests.post(f"http://{SERVER_IP}:{SERVER_PORT}/chat/sandMessage", headers=header, data=dataJ)
    data = r.json()
    if data['data'] == "messageSanded":
        GLchatID = data["chatID"]
def close_chat(e):
    page.appbar = None
    page.bottom_appbar = None
    page.clean()
    page.add(pageUI)
messangerUIheader = [ft.Text("lox")]
messageTextField = ft.TextField(expand=True, label="Сообщение")
messangerUIfotter = ft.Row([ft.IconButton(icon=ft.icons.EMOJI_EMOTIONS_OUTLINED, icon_size=userData["standart_text_size_h3"], icon_color=ft.colors.PRIMARY), messageTextField, ft.IconButton(icon=ft.icons.SEND, icon_size=userData["standart_text_size_h3"], icon_color=ft.colors.PRIMARY, on_click=send_message)])
def openChat(chatID):
    global GLchatID, nnn
    nnn = False
    GLchatID = chatID
    header = {"my_id": userData["account"]["id"], "deviceID": str(userData["deviceID"]), "chatID":chatID}
    r = requests.get(f"http://{SERVER_IP}:{SERVER_PORT}/chat/info", headers=header)
    data = r.json()
    generateChatPage(data['tag'])
    #тут будет добавление элементов с сообщениями
def generateChatPage(name):
    page.clean()
    page.appbar = ft.AppBar(
        bgcolor=ft.colors.ON_PRIMARY,
        center_title=True,
        title=ft.Text(name, size=userData["standart_text_size_h2"], color=ft.colors.PRIMARY),
        leading=ft.IconButton(ft.icons.SUBDIRECTORY_ARROW_LEFT,icon_size=userData["standart_text_size_h2"], icon_color=ft.colors.PRIMARY, on_click=close_chat),
        actions=messangerUIheader
    )
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.PRIMARY_CONTAINER,
        content=messangerUIfotter
    )
    page.update()


MyChats = None
def search(e):
    header = {"my_id": userData["account"]["id"], "deviceID": str(userData["deviceID"]), "search":str(search_textField.value)}
    r = requests.get(f"http://{SERVER_IP}:{SERVER_PORT}/search/user", headers=header)
    data = r.json()
    f_el = ft.Row([ft.IconButton(icon=ft.icons.CLOSE, icon_size=userData["standart_text_size_h2"],icon_color=ft.colors.ON_PRIMARY, on_click=close_search),search_textField, ft.IconButton(icon=ft.icons.SEARCH, icon_size=userData["standart_text_size_h2"], icon_color=ft.colors.ON_PRIMARY, on_click=search)],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    array = [f_el]
    for el in data["results"]:
        if data["results"][el]["chat"] != None:array.append(ft.Container(content=ft.Row([ft.Icon(ft.icons.CHAT, size=userData["standart_text_size_h3"], color=ft.colors.ON_PRIMARY), ft.Text(data["results"][el]["tag"], color=ft.colors.ON_PRIMARY, size=userData["standart_text_size_h4"])], spacing=15), on_click=open_old_chat, data=data["results"][el]["chat"]))
        else: array.append(ft.Container(content=ft.Row([ft.Icon(ft.icons.CHAT, size=userData["standart_text_size_h3"], color=ft.colors.ON_PRIMARY), ft.Text(data["results"][el]["tag"], color=ft.colors.ON_PRIMARY, size=userData["standart_text_size_h4"])], spacing=15),data=el, on_click=open_new_chat))
    search_UI.content = ft.Column(array)
    page.update()
def on_chat_click(e):
    chatId = e.control.data
    openChat(chatId)
def open_old_chat(e):
    openChat(e.control.data)
def open_new_chat(e):
    global nnn, GLchatID
    nnn=True
    GLchatID=e.control.data
    generateChatPage(e.control.data)
def close_search(e):
    search_UI.visible = False
    page.update()
def chats():
    chats = []
    header = {"my_id": userData["account"]["id"], "deviceID": str(userData["deviceID"])}
    r = requests.get(f"http://{SERVER_IP}:{SERVER_PORT}/get_my_chats", headers=header)
    data = r.json()
    for el in data["chatList"]:
        title = "None"
        if data["chatList"][el]["user1ID"] == userData["account"]["id"]:
            title = data["chatList"][el]["user2ID"]
        elif data["chatList"][el]["user2ID"] == userData["account"]["id"]:
            title = data["chatList"][el]["user1ID"]
        chats.append(ft.Container(content=ft.Container(content=ft.Row([ft.Column([ft.Text(title, size=25, color=ft.colors.PRIMARY), ft.Text(data["chatList"][el]["lastMessage"], size=15, color=ft.colors.SECONDARY)])]), margin=ft.margin.symmetric(horizontal=15, vertical=5)), bgcolor=ft.colors.PRIMARY_CONTAINER, data=el, on_click=on_chat_click))
    return chats
search_UI = ft.Container(content=None, margin=ft.margin.only(right=3, left=15), padding=ft.padding.symmetric(vertical=3, horizontal=5), visible=False, bgcolor=ft.colors.ON_SECONDARY_CONTAINER, border=ft.border.all(3, ft.colors.OUTLINE_VARIANT), border_radius=7)
search_textField = ft.TextField(label="Поиск", color=ft.colors.ON_PRIMARY, border_color=ft.colors.ON_PRIMARY, cursor_color=ft.colors.PRIMARY_CONTAINER, focused_bgcolor=ft.colors.ON_PRIMARY_CONTAINER, text_size=userData["standart_text_size_h6"], adaptive=True)
def init():
    global pageUI, MyChats, search_UI
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.colors.BACKGROUND
    page.window_min_width = 400
    page.window_min_height = 200
    MyChats = chats()
    nnUI = ft.Column(
        [
            ft.Container(
                content=header,
                bgcolor=ft.colors.ON_PRIMARY,
                margin=ft.margin.only(bottom=5, left=0, right=0, top=0),
                height=60,
                padding=ft.padding.symmetric(horizontal=15, vertical=5)
            ),
            ft.Container(
                content=ft.Column(MyChats, spacing=3),
                margin=ft.margin.only(bottom=5, left=1, right=1, top=0),
                bgcolor=ft.colors.OUTLINE
            )

        ]
    )
    pages.mobile.overlay_menu.overlay.margin = ft.margin.only(right=page.window_width*0.3, bottom=page.window_height*0.1)
    search_UI.content = ft.Column([ft.Row([ft.IconButton(icon=ft.icons.CLOSE, icon_size=userData["standart_text_size_h2"], icon_color = ft.colors.ON_PRIMARY, on_click=close_search), search_textField, ft.IconButton(icon=ft.icons.SEARCH, icon_size=userData["standart_text_size_h2"], icon_color=ft.colors.ON_PRIMARY, on_click=search)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)])
    pageUI = ft.Stack(
        controls=[
            nnUI,
            search_UI,
            pages.mobile.overlay_menu.overlay
        ]
    )
    pages.mobile.overlay_menu.overlay.visible = False

