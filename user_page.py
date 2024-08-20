import flet as ft

from flet_route import Params, Basket

def UserPage(page: ft.Page, params: Params, basket: Basket):

    def intro_action(e):
        print(e)
        page.go("/home")

    user_text_field = ft.TextField(
        label="Usuario"
    )

    intro_button = ft.FloatingActionButton(
        text="Enter",
        on_click=intro_action
    )

    central_widget = ft.Container(
        content=[user_text_field, intro_button] ,
        expand=True
    )

    page.views.append(ft.View("/", controls=[central_widget]))
    page.update()