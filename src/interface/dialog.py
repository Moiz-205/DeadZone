import flet as ft
from datetime import datetime
from interface import buttons
from utils import helpers

def create_title_field():
    return ft.TextField(
        hint_text="What needs to be done?",
        expand=True
    )

def create_start_date_field():
    date_picker = helpers.create_date_picker_control()

    date_field = ft.TextField(
        label="Start Date",
        value=datetime.now().strftime("%Y-%m-%d"),
        hint_text="YYYY-MM-DD",
        expand=True
    )

    def on_date_selected(e):
        if date_picker.value:
            date_field.value = date_picker.value.strftime("%Y-%m-%d")
            date_field.update()

    date_picker.on_change = on_date_selected

    cal_button = ft.IconButton(
        icon=ft.Icons.CALENDAR_TODAY,
        on_click=lambda e: setattr(date_picker, 'open', True) or date_picker.update()
    )
    row = ft.Row([date_field, cal_button])

    return row, date_picker

def create_end_date_field():
    date_picker = helpers.create_date_picker_control()

    date_field = ft.TextField(
        label="End Date",
        hint_text="YYYY-MM-DD",
        expand=True
    )
    def on_date_selected(e):
        if date_picker.value:
            date_field.value = date_picker.value.strftime("%Y-%m-%d")
            date_field.update()

    date_picker.on_change = on_date_selected

    cal_button = ft.IconButton(
        icon=ft.Icons.CALENDAR_TODAY,
        on_click=lambda e: setattr(date_picker, 'open', True) or date_picker.update()
    )
    row = ft.Row([date_field, cal_button])

    return row, date_picker


def create_input_dialog(title_field, start_date_field, end_date_field, cancel_handler, add_handler):
    dialog_buttons = buttons.create_dialog_buttons(cancel_handler, add_handler)

    content = ft.Column([
        title_field,
        start_date_field,
        end_date_field
    ])
    dialog = ft.AlertDialog(
        title=ft.Text("Create a new deadline."),
        content=content,
        actions=list(dialog_buttons)
    )
    return dialog
