import flet as ft
from ui.layout import build_ui

def main(page: ft.Page):
        page.tittle = "CONVERSOR DE MONEDAS"
        page.window_width = 400
        page.window_heigth = 400
        page.scroll = ft.ScrollMode.AUTO
        build_ui(page)

if __name__ == "__main__":
        ft.app(target=main)