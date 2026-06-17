import flet as ft
from interface import container

from utils.config import WINDOW_WIDTH, WINDOW_HEIGHT, BG_COLOR

def main(page: ft.Page):
    page.window.width = WINDOW_WIDTH
    page.window.height = WINDOW_HEIGHT
    page.bgcolor = BG_COLOR

    input_task = ft.TextField(
        hint_text="What needs to be done?",
        expand=True
    )

    def cancel_button(e):
        input_overlay.open = False
        page.update()

    def add_button(e):
        print(input_task.value)
        input_overlay.open = False
        input_task.value = ""
        page.update()

    def add_task(e):
        print("FAB clicked.")
        input_overlay.open = True
        page.update()


    input_overlay = ft.AlertDialog(
        title=ft.Text("Create a new deadline."),
        content=input_task,
        actions=([
            ft.TextButton("Cancel", on_click=cancel_button),
            ft.TextButton("Add", on_click=add_button)
        ]),
        open=False
    )

    page.overlay.append(input_overlay)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=add_task, align=ft.Alignment.BOTTOM_CENTER
    )

    test_box = container.create_task_box(page, "Research", "2024-01-01", "2024-02-01")
    page.add(test_box)


ft.run(main)
