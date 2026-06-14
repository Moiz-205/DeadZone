import flet as ft


def main(page: ft.Page):
    page.window.width = 600
    page.window.height = 400
    page.bgcolor = ft.Colors.WHITE_12
    # counter = ft.Text("0", size=50, data=0)

    input_task = ft.TextField(
        hint_text="What needs to be done?",
        expand=True
    )

    def add_task(e):
        input_overlay.open = True
        page.update()

    def cancel_button(e):
        input_overlay.open = False
        page.update()

    def add_button(e):
        print(input_task.value)
        input_overlay.open = False
        input_task.value = ""
        page.update()

    input_overlay = ft.AlertDialog(
        title=ft.Text("Create a new deadline."),
        content=input_task,
        actions=([
            ft.TextButton("Cancel", on_click=cancel_button),
            ft.TextButton("Add", on_click=add_button)
        ])
    )

    page.overlay.append(input_overlay)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=add_task, align=ft.Alignment.BOTTOM_CENTER
    )

    test_box = ft.Container(
        content=ft.Column([
            ft.Text("Research", size=20),
            ft.Row([
                ft.Text("Start: 2024-01-01", size=10),
                ft.Text("End: 2024-02-01", size=10)
            ], spacing=20)  # space between dates
        ]),
        height=120,
        width=600,
        # expand=True,
        border_radius=10,
        bgcolor=ft.Colors.BLUE_GREY_100
    )

    page.add(test_box)


ft.run(main)
