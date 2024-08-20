import flet as ft

from flet_route import Routing, path

from number_game import NumberGamePage
from tres_en_raya import TresEnRayaPage
from home_page import HomePage
#from user_page import UserPage

def setup_page(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 50
    #page.window.width = 400
    #page.window.height = 450

def main(page: ft.Page):
    setup_page(page)
    
    app_routes = [
        #path(url="/", view=UserPage, clear=True),
        path(url="/home", view=HomePage, clear=True),
        path(url="/tres_en_raya", view=TresEnRayaPage, clear=True),
        path(url="/number_game", view=NumberGamePage, clear=True),
    ]

    Routing(
        page=page,
        app_routes=app_routes,
    )

    page.go("/home")

if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER
    )
