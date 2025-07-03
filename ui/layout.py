import flet as ft
from services.currency_service import convertir_moneda
from utils.validators import validar_monto

def build_ui(page: ft.Page):
    origen = ft.TextField(label="Moneda origen (ej: USD)", value="USD")
    destino = ft.TextField(label="Moneda destino (ej: EUR)")
    monto_input = ft.TextField(label="Monto", keyboard_type=ft.KeyboardType.NUMBER)
    resultado = ft.Text("")

    def on_convertir(e):
        origen_moneda = origen.value.strip().upper()
        destino_moneda = destino.value.strip().upper()
        if not validar_monto(monto_input.value):
            resultado.value = "Monto inválido."
            page.update()
            return

        monto = float(monto_input.value)
        resultado_conversion = convertir_moneda(origen_moneda, destino_moneda, monto)
        if resultado_conversion is not None:
            resultado.value = f"{monto} {origen_moneda} = {round(resultado_conversion, 2)} {destino_moneda}"
        else:
            resultado.value = "Error en la conversión. ¿Códigos de moneda correctos?"
        page.update()

    page.add(
        ft.Column([
            ft.Text("💱 Conversor de Monedas", size=24, weight=ft.FontWeight.BOLD),
            origen,
            destino,
            monto_input,
            ft.ElevatedButton("Convertir", on_click=on_convertir),
            resultado
        ], spacing=20)
    )
