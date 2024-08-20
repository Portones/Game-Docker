import flet as ft

from flet_route import Params, Basket

def HomePage(page: ft.Page, params: Params, basket: Basket):

    def change_game(e):
        clicked_button = e.control
        route = f"/tres_en_raya" if clicked_button.data == "Tres" else f"/number_game"
        page.go(route)
        page.update()

    button_tres_raya = ft.FloatingActionButton(text="Tres en Raya", width=150, on_click=change_game, data="Tres")
    button_number_game = ft.FloatingActionButton(text="Number Game", width=150, on_click=change_game, data="Number")
    all_button_widget = ft.Row([button_tres_raya, button_number_game], vertical_alignment="center", alignment="center")

    central_widget = ft.Container(
        content=all_button_widget,
        expand=True
    )

    page.views.append(ft.View("/home", controls=[central_widget]))
    page.update()