import flet as ft
from interface import dialog, layout, buttons
from core import handlers, data

from utils.config import WINDOW_WIDTH, WINDOW_HEIGHT, BG_COLOR

def main(page: ft.Page):
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.bgcolor = BG_COLOR

    ## Interface components
    input_field = dialog.create_input_field()
    tasks_column = layout.create_tasks_layout(page, tasks=data.get_tasks())

    ## Button handlers components
    cancel_handler = handlers.cancel_dialog_button(page)
    add_handler = handlers.add_dialog_button(page, input_field, tasks_column, layout)
    fab_handler = handlers.open_dialog_button(page)

    ## Overlay componet
    input_dialog = dialog.create_input_dialog(input_field, cancel_handler, add_handler)

    ## Main screen
    page.overlay.append(input_dialog)
    page.floating_action_button = buttons.create_fab_button(fab_handler)
    page.add(tasks_column)

ft.run(main)
