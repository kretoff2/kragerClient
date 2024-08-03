import flet as ft
import json
import time
import requests

SERVER_IP = "localhost"
SERVER_PORT = 80

page:ft.Page
enable_nav_bar = True
userData:json

user_cod = ft.TextField(label='Код', width=300, color=ft.colors.AMBER_900)
ErrorMessage = ft.Text("",color=ft.colors.RED)

enable_cod = False
my_id = 0
def save_data():
    with open('data.json', 'w') as f:
        json.dump(userData, f)
def register(e):
    global enable_cod
    global my_id
    btn_reg.scale = 0.5
    if user_cod.value == "" and enable_cod == False:
        body = {"email":user_email.value}
        bodyJ = json.dumps(body)
        r = requests.post(f"http://{SERVER_IP}:{SERVER_PORT}/sandReg", data=bodyJ)
        if r.json()["data"]=="message_sanded":
            ErrorMessage.value = "К вам на почту выслано письмо м кодом"
            ErrorMessage.color = ft.colors.WHITE
            page.add(ft.Row([user_cod], alignment=ft.MainAxisAlignment.CENTER))
            enable_cod = True
            my_id = r.json()["your_id"]
        else:
            ErrorMessage.value = "При отправлении сообщения произошла ошибка, проверьте правильно ли вы вписали ее"
    else:
        body = {"cod": user_cod.value, "tag": user_login.value, "password": user_pass.value, "email": user_email.value, "id": my_id}
        bodyJ = json.dumps(body)
        r = requests.post(f"http://{SERVER_IP}:{SERVER_PORT}/reg", data=bodyJ)
        data = r.json()
        if data['data'] == 'goodRegistration':
            userData['staticKey'] = data['key']
            userData["account"]["active"] = True
            userData["account"]["tag"] = data["tag"]
            userData["account"]["email"] = data["email"]
            userData["account"]["id"] = data["id"]
            save_data()
        elif data['data'] == 'invalidLogin':
            ErrorMessage.value = 'Это имя пользователя уже занято'
            ErrorMessage.color = ft.colors.RED
        elif data['data'] == 'invalidEmail':
            ErrorMessage.value = 'На эту электронную почту уже зарегестрирован аккаунт'
            ErrorMessage.color = ft.colors.RED
        elif data['data'] == 'wrongCode':
            ErrorMessage.value = 'Неверный код'
            ErrorMessage.color = ft.colors.RED
    page.update()
    time.sleep(0.1)
    btn_reg.scale = 1
    page.update()

def log_in(e):
    btn_log.scale = 0.5
    data = {"tag": user_login.value, "password": user_pass.value}
    dataJ = json.dumps(data)
    r = requests.post(f"http://{SERVER_IP}:{SERVER_PORT}/login", data=dataJ)
    data = r.json()
    if data["data"] == "goodLogin":
        userData["staticKey"] = data["key"]
        userData["deviceID"] = data["deviceID"]
        userData["account"]["active"] = True
        userData["account"]["name"] = data["userInfo"]["login"]
        userData["account"]["tag"] = data["userInfo"]["tag"]
        userData["account"]["email"] = data["userInfo"]["email"]
        userData["account"]["number"] = data["userInfo"]["num"]
        userData["account"]["id"] = data["userInfo"]["userID"]
        save_data()
    elif data['data'] == 'invalidLoginOrPassword':
        ErrorMessage.value = 'Неверное имя пользователя или пароль'
        ErrorMessage.color = ft.colors.RED
    else:
        ErrorMessage.value = 'Не известная ошибка'
    page.update()
    time.sleep(0.1)
    btn_log.scale = 1
    page.update()
btn_reg = ft.Container(
    content=ft.Row([ft.Text(value='Зарегестрироваться', color=ft.colors.AMBER_900, size=15)], alignment=ft.MainAxisAlignment.CENTER),
    border_radius=ft.BorderRadius(5,5,5,5),
    bgcolor=ft.colors.DEEP_PURPLE_800,
    width=300,
    height=50,
    animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
    on_click=register,
    disabled=True
)
btn_log = ft.Container(
    content=ft.Row([ft.Text(value='Войти', color=ft.colors.AMBER_900, size=15)], alignment=ft.MainAxisAlignment.CENTER),
    border_radius=ft.BorderRadius(5,5,5,5),
    bgcolor=ft.colors.DEEP_PURPLE_800,
    width=300,
    height=50,
    animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
    on_click=log_in,
    disabled=True
)
def validate(e):
    if all([user_login.value, user_pass.value, user_pass_double.value, user_email.value]):
        btn_reg.disabled = False
        btn_log.disabled = False
    elif all([user_login.value, user_pass.value]):
        btn_log.disabled = False
        btn_reg.disabled = True
    else:
        btn_reg.disabled = True
        btn_log.disabled = True
    page.update()

user_login = ft.TextField(label='Логин', width=300, on_change=validate, color=ft.colors.AMBER_900)
user_pass = ft.TextField(label='Пароль', width=300, on_change=validate, password=True, color=ft.colors.AMBER_900)
user_pass_double = ft.TextField(label='Повторите пароль', width=300, on_change=validate, password=True, color=ft.colors.AMBER_900)
user_email = ft.TextField(label='email', width=300, on_change=validate, color=ft.colors.AMBER_900)

rerister_ui = ft.Row(
    [
        ft.Column(
            [
                ft.Text('Регистрация', size=25),
                user_login,
                user_pass,
                user_pass_double,
                user_email,
                btn_reg,
                ErrorMessage
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
)
log_in_ui = ft.Row(
    [
        ft.Column(
            [
                ft.Text('Вход', size=28),
                user_login,
                user_pass,
                btn_log,
                ErrorMessage
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    ],
    alignment=ft.MainAxisAlignment.CENTER
)


def navigate(e):
    index = page.navigation_bar.selected_index
    page.clean()

    if index == 0:
        page.add(rerister_ui)
    elif index == 1:
        page.add(log_in_ui)

nav_bar = ft.NavigationBar(
    destinations=[
        ft.NavigationDestination(icon=ft.icons.VERIFIED_USER, label="Регистрация"),
        ft.NavigationDestination(icon=ft.icons.VERIFIED_USER_OUTLINED, label="Вход")
    ], on_change=navigate
)
pageUI = rerister_ui