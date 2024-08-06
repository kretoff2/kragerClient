from flet import ScrollMode
from pages import data
def open_page(now_page, page, userData):
    page.scroll = ScrollMode.AUTO
    now_page.page = page
    data.userData = userData
    now_page.init()
    page.clean()
    page.add(now_page.pageUI)
    if now_page.enable_nav_bar == True:
        page.navigation_bar = now_page.nav_bar
    else:
        if page.navigation_bar != None:
            page.navigation_bar.clean()
    page.update()