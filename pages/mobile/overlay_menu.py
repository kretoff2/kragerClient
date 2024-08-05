import flet as ft

page:ft.Page
def close_overlay(e):
    overlay.visible=False
    page.update()

column1 = ft.Column(
    [
        ft.IconButton(icon=ft.icons.CLEAR, icon_size=30, on_click=close_overlay, icon_color=ft.colors.ON_PRIMARY),
        ft.Container(content=ft.Row([ft.Icon(name=ft.icons.HOME, size=35, color=ft.colors.ON_PRIMARY), ft.Text(value="Меню", size=25, color=ft.colors.ON_PRIMARY)]), margin=ft.margin.symmetric(vertical=0), bgcolor=ft.colors.PRIMARY),
        ft.Container(content=ft.Row([ft.Icon(name=ft.icons.SETTINGS, size=35, color=ft.colors.ON_PRIMARY), ft.Text(value="Настройки", size=25, color=ft.colors.ON_PRIMARY)]), margin=ft.margin.symmetric(vertical=0), bgcolor=ft.colors.PRIMARY)
    ], spacing=1
)
overlay = ft.Container(content=column1, bgcolor=ft.colors.ON_SECONDARY_CONTAINER, visible=False, expand=True, alignment=ft.alignment.top_left, border=ft.border.all(1, color=ft.colors.OUTLINE_VARIANT))