import flet as ft
from interface import container, dialog, buttons

def render_tasks(page, tasks, tasks_column):
    tasks_column.controls.clear()
    for task in reversed(tasks):
        task_item = container.create_task_container(
            page,
            task["title"],
            task["start_date"],
            task["end_date"]
        )
        tasks_column.controls.append(task_item)

def create_tasks_layout(page, tasks):
    tasks_column = ft.Column(
        controls=[],
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )
    render_tasks(page, tasks, tasks_column)

    return tasks_column

def setup_interface(page, cancel_handler, add_handler, fab_handler, tasks):
    input_field = dialog.create_input_field()
    input_dialog = dialog.create_input_dialog(input_field, cancel_handler, add_handler)
    fab = buttons.create_fab_button(fab_handler)
    tasks_column = create_tasks_layout(page, tasks)

    return {
        "input_field": input_field,
        "input_dialog": input_dialog,
        "fab": fab,
        "tasks_column": tasks_column
    }
