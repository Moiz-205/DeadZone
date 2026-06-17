import flet as ft

from utils.config import TEXT_COLOR, CONTAINER_BG_COLOR, CONTAINER_DROP_SHADOW



def create_task_box(page, title, start_date, end_date):
    expanded = False

    def on_box_click(e):
        nonlocal expanded
        expanded = not expanded
        test_box.height = 220 if expanded else 120
        update_box_content()

    def update_box_content():
        column_items = [
            ft.Text(title, size=40, color=TEXT_COLOR,
                text_align=ft.TextAlign.CENTER),
            ft.Row([
                ft.Text(f"Start: {start_date}", size=20, color=TEXT_COLOR),
                ft.Text(f"End: {end_date}", size=20, color=TEXT_COLOR)
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ]

        if expanded:
            column_items.append(ft.Divider())
            column_items.append(ft.Text("Progress bar", size=12))
            column_items.append(ft.Text("Time Remaining", size=12))

        box_content.controls = column_items
        page.update()

    box_content = ft.Column([], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    update_box_content()

    test_box = ft.Container(
        content=box_content,
        height=120,
        width=600,
        border_radius=10,
        bgcolor=CONTAINER_BG_COLOR,
        shadow=ft.BoxShadow(blur_radius=5, color=CONTAINER_DROP_SHADOW),
        padding=15,
        on_click=on_box_click
    )

    return test_box
