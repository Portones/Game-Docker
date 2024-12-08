import flet as ft
import yaml

from flet_route import Params, Basket

def HomePage(page: ft.Page, params: Params, basket: Basket):

    def change_game(e):
        clicked_button = e.control
        route = f"/tres_en_raya" if clicked_button.data == "Tres" else f"/number_game"
        page.go(route)
        page.update()

    def check_user(e):
        user = username_widget.value
        with open("users.yaml", "r") as f:
            data = yaml.safe_load(f) or {}
        if user in data:
            actual_level = data[user]
        else:
            actual_level = 1
            data[user] = 1
        with open("users.yaml", "w") as f:
            yaml.dump(data, f, default_flow_style=False)

    
    button_tres_raya = ft.FloatingActionButton(text="Tres en Raya", width=150, on_click=change_game, data="Tres", disabled=True)
    button_number_game = ft.FloatingActionButton(text="Number Game", width=150, on_click=change_game, data="Number", disabled=True)
    game_widget = ft.Row([
            button_tres_raya, button_number_game
        ], 
        vertical_alignment="center",
        alignment="center")
    
    username_widget = ft.TextField(label="User")
    user_widget = ft.Row(
        controls=[
            username_widget,
            ft.FloatingActionButton(text="Enter", on_click=check_user)
        ], vertical_alignment="center", alignment="center"
    )

    all_button_widget = ft.Column([
            user_widget, game_widget
        ], 
        horizontal_alignment="center",
        alignment="center")

    central_widget = ft.Container(
        content=all_button_widget,
        expand=True
    )

    page.views.append(ft.View("/home", controls=[central_widget]))
    page.update()