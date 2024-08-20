import flet as ft
from random import randint

from flet_route import Params, Basket

def NumberGamePage(page: ft.Page, params: Params, basket: Basket):
    min_number = 0
    max_number = 9
    counter = 0
    max_tries = 6

    def reset_game():
        nonlocal counter

        counter = 0
        for button in button_play_list:
            button.bgcolor = None
            button.data = 0
            button.text = button.data
            button.update()

        for button in button_sol_list:
            button.data = randint(min_number, max_number)
            button.update()

    def check_win():
        nonlocal counter

        results = [button_play.bgcolor == ft.colors.GREEN for button_play in button_play_list]
        if sum(results) == len(results):
            dialog.title=ft.Text(f"¡Has ganado!😀")
            page.open(dialog)
        else:
            if counter == max_tries:
                dialog.title=ft.Text(f"¡Has perdido!😢")
                page.open(dialog)
        counter += 1

    def check_restults(e):

        solution_values = [button.data for button in button_sol_list]
        for index, button_play in enumerate(button_play_list):
            player_number = button_play.data
            if player_number == button_sol_list[index].data:
                button_play.bgcolor = ft.colors.GREEN
            elif player_number in solution_values:
                button_play.bgcolor = ft.colors.ORANGE
            else:
                button_play.bgcolor = ft.colors.RED
            button_play.update()
            
        check_win()
        
    def change_button_number(e):
        clicked_button = e.control
        if clicked_button.data < max_number:
            clicked_button.data += 1
        else:
            clicked_button.data = 0

        clicked_button.text = clicked_button.data
        clicked_button.update()
    
    texto_widget = ft.Text("Number Game", size = 20, weight=ft.FontWeight.BOLD)
    home_button = ft.FloatingActionButton(icon=ft.icons.HOME, on_click=lambda e: page.go("/home"))

    dialog = ft.AlertDialog(title=ft.Text(f"¡Has ganado!😀"), on_dismiss=lambda e: reset_game())

    button_sol_1 = ft.FloatingActionButton(icon=ft.icons.QUESTION_MARK, data=None)
    button_sol_2 = ft.FloatingActionButton(icon=ft.icons.QUESTION_MARK, data=None)
    button_sol_3 = ft.FloatingActionButton(icon=ft.icons.QUESTION_MARK, data=None)
    button_sol_4 = ft.FloatingActionButton(icon=ft.icons.QUESTION_MARK, data=None)

    button_play_1 = ft.FloatingActionButton(text=0, data=0, on_click=change_button_number)
    button_play_2 = ft.FloatingActionButton(text=0, data=0, on_click=change_button_number)
    button_play_3 = ft.FloatingActionButton(text=0, data=0, on_click=change_button_number)
    button_play_4 = ft.FloatingActionButton(text=0, data=0, on_click=change_button_number)

    button_play_list = [button_play_1, button_play_2, button_play_3, button_play_4]
    button_sol_list = [button_sol_1, button_sol_2, button_sol_3, button_sol_4]

    for button in button_sol_list:
        button.data = randint(min_number, max_number)
        
    play_button = ft.FloatingActionButton(text="Play", on_click=check_restults, width=80)

    central_widget = ft.Container(
        ft.Column(
            controls=[
                ft.Row([texto_widget, home_button], spacing=20, vertical_alignment="center", alignment="center"),
                ft.Row([button_sol_1, button_sol_2, button_sol_3, button_sol_4], vertical_alignment="center", alignment="center"),
                ft.Row([button_play_1, button_play_2, button_play_3, button_play_4], vertical_alignment="center", alignment="center"),
                play_button
            ],
            horizontal_alignment="center",
            alignment="center"
        )
    )

    page.views.append(ft.View("/number_game", controls=[central_widget]))
    page.update()
