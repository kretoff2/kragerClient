import flet as ft
from flet_contrib.color_picker import ColorPicker

import json
import time

from pages import open_page, data
from pages.mobile import menu
import requests
name = "global_settings"
def save_data():
    with open('data.json', 'w') as f:
        json.dump(userData, f)

SERVER_IP = "localhost"
SERVER_PORT = 80

page:ft.Page
enable_nav_bar = False
userData = data.userData

menuUI = ft.Container(bgcolor=ft.colors.TERTIARY, visible=False, content=None, margin=ft.margin.symmetric(vertical=40, horizontal=20), padding=ft.padding.all(10))

pageUI = None
def close_overlay_menu(e):
    menuUI.visible = False
    page.update()
picker = ColorPicker(color="#000000", width=300)
def view_palitr(e):
    page.theme = ft.Theme(color_scheme_seed=picker.color)
    page.update()
def change_color(e):
    page.theme = ft.Theme(color_scheme_seed=picker.color)
    userData["color_theme"] = picker.color
    save_data()
    page.update()
def set_text_size(e):
    userData["veiw_text_size"] = slider.value
    userData["standart_text_size_h1"] = slider.value*2
    userData["standart_text_size_h2"] = slider.value*1.6
    userData["standart_text_size_h3"] = slider.value*1.4
    userData["standart_text_size_h4"] = slider.value
    userData["standart_text_size_h5"] = slider.value*0.8
    userData["standart_text_size_h6"] = slider.value*0.6
    userData["standart_text_size_l"] = slider.value*0.3
    data.userData = userData
    save_data()
    resize()
    page.clean()
    page.add(pageUI)
    page.update()
slider = ft.Slider(min=1, max=50, divisions=49, active_color=ft.colors.ON_TERTIARY_CONTAINER, label="{value} размер",
              thumb_color=ft.colors.PRIMARY, data="{value}", value=userData["veiw_text_size"], on_change=set_text_size)

viewUI = None
def open_view_menu(e):
    slider.value = userData["veiw_text_size"]+1
    set_text_size(e)
    menuUI.content = viewUI
    menuUI.visible = True
    page.update()

def go_to_menu(e):
    open_page.open_page(menu, page, userData)

UI = None
def resize():
    global viewUI, UI, pageUI
    viewUI = ft.Column(
    [
        ft.IconButton(icon = ft.icons.CLOSE, icon_size=userData["standart_text_size_h1"], icon_color=ft.colors.ON_TERTIARY, bgcolor=ft.colors.TERTIARY, on_click=close_overlay_menu),
        ft.Row([
            ft.Icon(name=ft.icons.TEXT_FIELDS, size=userData["standart_text_size_h3"], color=ft.colors.ON_TERTIARY),
            ft.Text(value="Размер текста", size=userData["standart_text_size_h4"], color=ft.colors.ON_TERTIARY)
        ]),
        slider,
        ft.Text(value="Цвет системы", size=userData["standart_text_size_h4"], color=ft.colors.ON_TERTIARY),
        picker,
        ft.Container(content=ft.Text("Посмотреть палитру", color=ft.colors.ON_TERTIARY_CONTAINER, size=userData["standart_text_size_h4"]), bgcolor=ft.colors.TERTIARY_CONTAINER, height=userData["standart_text_size_h4"]*2, width=userData["standart_text_size_h4"]*7.2, border_radius=15, alignment=ft.alignment.center, on_click=view_palitr),
        ft.Container(content=ft.Text("Установить палитру", color=ft.colors.ON_TERTIARY_CONTAINER, size=userData["standart_text_size_h4"]), bgcolor=ft.colors.TERTIARY_CONTAINER, height=userData["standart_text_size_h4"]*2, width=userData["standart_text_size_h4"]*7.2, border_radius=15, alignment=ft.alignment.center, on_click=change_color),
        ft.Text("Палитра цветов", size=userData["standart_text_size_h3"], color=ft.colors.ON_TERTIARY),
        ft.Container(
            content=ft.Row(
            [
                ft.Container(height=100, width=100, bgcolor=ft.colors.PRIMARY),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_PRIMARY),
                ft.Container(height=100, width=100, bgcolor=ft.colors.PRIMARY_CONTAINER),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_PRIMARY_CONTAINER),
                ft.Container(height=100, width=100, bgcolor=ft.colors.SECONDARY),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_SECONDARY),
                ft.Container(height=100, width=100, bgcolor=ft.colors.SECONDARY_CONTAINER),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_SECONDARY_CONTAINER),
                ft.Container(height=100, width=100, bgcolor=ft.colors.TERTIARY),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_TERTIARY),
                ft.Container(height=100, width=100, bgcolor=ft.colors.TERTIARY_CONTAINER),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_PRIMARY_CONTAINER),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ERROR),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_ERROR),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ERROR_CONTAINER),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_ERROR_CONTAINER),
                ft.Container(height=100, width=100, bgcolor=ft.colors.OUTLINE),
                ft.Container(height=100, width=100, bgcolor=ft.colors.OUTLINE_VARIANT),
                ft.Container(height=100, width=100, bgcolor=ft.colors.BACKGROUND),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_BACKGROUND),
                ft.Container(height=100, width=100, bgcolor=ft.colors.SURFACE),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_SURFACE),
                ft.Container(height=100, width=100, bgcolor=ft.colors.SURFACE_TINT),
                ft.Container(height=100, width=100, bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_SURFACE_VARIANT),
                ft.Container(height=100, width=100, bgcolor=ft.colors.INVERSE_SURFACE),
                ft.Container(height=100, width=100, bgcolor=ft.colors.ON_INVERSE_SURFACE),
                ft.Container(height=100, width=100, bgcolor=ft.colors.INVERSE_PRIMARY),
                ft.Container(height=100, width=100, bgcolor=ft.colors.SHADOW),
                ft.Container(height=100, width=100, bgcolor=ft.colors.SCRIM)
            ], alignment=ft.MainAxisAlignment.START, wrap=True
            ),
            bgcolor="#696969", padding=ft.padding.all(10)
        )
    ])
    UI = ft.Column(
    [
        ft.Container(content=ft.Row([ft.Icon(name=ft.icons.SETTINGS_OUTLINED, size=userData["standart_text_size_h1"], color=ft.colors.PRIMARY), ft.Text("Настройки",size=userData["standart_text_size_h2"], color=ft.colors.PRIMARY), ft.IconButton(icon=ft.icons.SUBDIRECTORY_ARROW_LEFT_SHARP, icon_size=userData["standart_text_size_h1"], icon_color=ft.colors.PRIMARY, on_click=go_to_menu)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), bgcolor=ft.colors.PRIMARY_CONTAINER),
        ft.Container(content=ft.Row([ft.Icon(name=ft.icons.COLOR_LENS, size=userData["standart_text_size_h3"], color=ft.colors.PRIMARY), ft.Text("Вид", color=ft.colors.PRIMARY, size=userData["standart_text_size_h4"])]), bgcolor=ft.colors.PRIMARY_CONTAINER, on_click=open_view_menu),
    ], spacing=2
    )
    pageUI = ft.Stack(
    controls=[
        UI,
        menuUI
    ]
)
def init():
    global picker
    page.bgcolor = ft.colors.BACKGROUND
    page.vertical_alignment = ft.MainAxisAlignment.START
    picker.color = userData["color_theme"]
    resize()