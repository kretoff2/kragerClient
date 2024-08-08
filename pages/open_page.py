from flet import ScrollMode
from pages import data
import json
def open_page(now_page, page, userData):
    page.scroll = ScrollMode.AUTO
    now_page.page = page
    userData["page"] = now_page.name
    with open('data.json', 'w') as f:
        json.dump(userData, f)
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
def open_page_with_name(now_page, page, userData):
    exec(f"from pages.mobile import {now_page}")
    exec(f"open_page({now_page}, page, userData)")