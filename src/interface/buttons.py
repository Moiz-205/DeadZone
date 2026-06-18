import flet as ft

def create_fab_button(fab_handler):
    fab = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        on_click=fab_handler,
        align=ft.Alignment.BOTTOM_CENTER
    )

    return fab

def create_dialog_buttons(cancel_handler, add_handler):
    return [
        ft.TextButton("Cancel", on_click=cancel_handler),
        ft.TextButton("Add", on_click=add_handler)
    ]
