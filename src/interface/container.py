import flet as ft

from utils.config import TEXT_COLOR, CONTAINER_BG_COLOR, CONTAINER_DROP_SHADOW

def build_task_content(title, start_date, end_date, expanded):
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

    return column_items

def handle_task_click(task_container, page, task_content, title, start_date, end_date):
    expanded = False

    def on_click(e):
        nonlocal expanded
        expanded = not expanded
        task_container.height = 220 if expanded else 120
        column_items = build_task_content(title, start_date, end_date, expanded)
        task_content.controls = column_items
        page.update()

    return on_click


def create_task_container(page, title, start_date, end_date):
    task_content = ft.Column(
        controls=[],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    task_container = ft.Container(
        content=task_content,
        height=120,
        width=600,
        border_radius=10,
        bgcolor=CONTAINER_BG_COLOR,
        shadow=ft.BoxShadow(blur_radius=5, color=CONTAINER_DROP_SHADOW),
        padding=15
    )

    column_items = build_task_content(
        title,
        start_date,
        end_date,
        expanded=False
    )

    task_content.controls = column_items

    task_container.on_click = handle_task_click(
        task_container,
        page,
        task_content,
        title,
        start_date,
        end_date
    )

    return task_container
