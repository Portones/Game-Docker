import flet as ft

from flet_route import Params, Basket

def TresEnRayaPage(page: ft.Page, params: Params, basket: Basket):
    cross_turn = True
    contador = 0

    def check_winner():
        winning_combinations = [
            [boton1, boton2, boton3],  # Primera fila
            [boton4, boton5, boton6],  # Segunda fila
            [boton7, boton8, boton9],  # Tercera fila
            [boton1, boton4, boton7],  # Primera columna
            [boton2, boton5, boton8],  # Segunda columna
            [boton3, boton6, boton9],  # Tercera columna
            [boton1, boton5, boton9],  # Diagonal principal
            [boton3, boton5, boton7]   # Diagonal secundaria
        ]

        for combo in winning_combinations:
            if combo[0].icon != ft.icons.NORTH and all(b.icon == combo[0].icon for b in combo):
                return combo[0].icon

        return None

    def change_button(e):
        nonlocal cross_turn
        nonlocal contador


        boton_pulsado = e.control

        if cross_turn:
            boton_pulsado.icon = ft.icons.CLOSE_OUTLINED
            boton_pulsado.icon_color = ft.colors.RED
        else:
            boton_pulsado.icon = ft.icons.CIRCLE_OUTLINED
            boton_pulsado.icon_color = ft.colors.BLUE

        cross_turn = not cross_turn
        contador += 1

        boton_pulsado.disabled = True
        boton_pulsado.update()
        texto_widget.value = f"Turno de {'Cruz' if cross_turn else 'Círculo'}"
        texto_widget.update()

        ganador = check_winner()
        if ganador:
            ganador_nombre = "Cruz" if ganador == ft.icons.CLOSE_OUTLINED else "Círculo"
            page.dialog = ft.AlertDialog(
                title=ft.Text(f"¡{ganador_nombre} ha ganado!"),
                on_dismiss=lambda e: reset_game()
            )
            page.dialog.open = True
            page.update()
        else:
            if contador == 9:
                page.dialog = ft.AlertDialog(
                    title=ft.Text(f"¡Empate!"),
                    on_dismiss=lambda e: reset_game()
                )
                page.dialog.open = True
                page.update()


    def reset_game():
        nonlocal cross_turn
        nonlocal contador

        for boton in [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9]:
            boton.icon = ft.icons.NORTH
            boton.disabled = False
            boton.icon_color = None
            boton.update()
            
        cross_turn = True
        contador = 0
        texto_widget.value = f"Turno de {'Cruz' if cross_turn else 'Círculo'}"
        texto_widget.update()


    texto_widget = ft.Text("Turno de Cruz", size=20, weight=ft.FontWeight.BOLD)
    home_button = ft.FloatingActionButton(icon=ft.icons.HOME, on_click=lambda e: page.go("/home"))
    boton1 = ft.FloatingActionButton(icon=ft.icons.NORTH, width=100, height=100, on_click=change_button, data="1")
    boton2 = ft.FloatingActionButton(icon=ft.icons.NORTH, width=100, height=100, on_click=change_button, data="2")
    boton3 = ft.FloatingActionButton(icon=ft.icons.NORTH, width=100, height=100, on_click=change_button, data="3")
    boton4 = ft.FloatingActionButton(icon=ft.icons.NORTH, width=100, height=100, on_click=change_button, data="4")
    boton5 = ft.FloatingActionButton(icon=ft.icons.NORTH, width=100, height=100, on_click=change_button, data="5")
    boton6 = ft.FloatingActionButton(icon=ft.icons.NORTH, width=100, height=100, on_click=change_button, data="6")
    boton7 = ft.FloatingActionButton(icon=ft.icons.NORTH, width=100, height=100, on_click=change_button, data="7")
    boton8 = ft.FloatingActionButton(icon=ft.icons.NORTH, width=100, height=100, on_click=change_button, data="8")
    boton9 = ft.FloatingActionButton(icon=ft.icons.NORTH, width=100, height=100, on_click=change_button, data="9")

    central_widget = ft.Container(
        ft.Column(
            controls=[
                ft.Row([texto_widget, home_button], spacing=20, vertical_alignment="center", alignment="center"),
                ft.Row([boton1, boton2, boton3], vertical_alignment="center", alignment="center"),
                ft.Row([boton4, boton5, boton6], vertical_alignment="center", alignment="center"),
                ft.Row([boton7, boton8, boton9], vertical_alignment="center", alignment="center")
            ],
            horizontal_alignment="center",
            alignment="center"
        )
    )

    page.views.append(ft.View("/tres_en_raya", controls=[central_widget]))
    page.update()
