import flet as ft
import json
import time
import requests

SERVER_IP = "localhost"
SERVER_PORT = 80

page:ft.Page
enable_nav_bar = False
userData:json

pageUI = None
header = ft.Container(
    content=ft.Row([ft.Icon(ft.icons.DENSITY_SMALL, color="#0059b8", size=25, animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)),ft.Text("Krager", size=25, color="#0059b8")], alignment=ft.MainAxisAlignment.CENTER,spacing=50)
)
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
        chats.append(ft.Container(content=ft.Container(content=ft.Row([ft.Column([ft.Text(title, size=25), ft.Text(data["chatList"][el]["lastMessage"], size=15, color="#666666")])]), margin=ft.margin.symmetric(horizontal=10, vertical=5)), bgcolor="#2b0b7d", margin=ft.margin.all(1)))
        return chats

def init():
    global pageUI
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "#001426"
    page.window_min_width = 400
    page.window_min_height = 200
    pageUI = ft.Column(
        [
            ft.Container(
                content=header,
                bgcolor="#002140",
                margin=ft.margin.only(bottom=5, left=1, right=1, top=0),
                height=60,
            ),
            ft.Container(
                content=ft.Column(chats()),
                margin=ft.margin.only(bottom=5, left=1, right=1, top=0),
                bgcolor=ft.colors.WHITE
            )

        ]
    )

