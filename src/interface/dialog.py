import flet as ft
from interface import buttons

def create_input_field():
    return ft.TextField(
        hint_text="What needs to be done?",
        expand=True
    )

def create_input_dialog(input_field, cancel_handler, add_handler):
    dialog_buttons = buttons.create_dialog_buttons(cancel_handler, add_handler)
    dialog = ft.AlertDialog(
        title=ft.Text("Create a new deadline."),
        content=input_field,
        actions=list(dialog_buttons)
    )
    return dialog
