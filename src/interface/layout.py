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
    title_field = dialog.create_title_field()
    start_date_field, start_date_picker = dialog.create_start_date_field()
    end_date_field, end_date_picker = dialog.create_end_date_field()
    input_dialog = dialog.create_input_dialog(
        title_field,
        start_date_field,
        end_date_field,
        cancel_handler,
        add_handler
    )
    fab = buttons.create_fab_button(fab_handler)
    tasks_column = create_tasks_layout(page, tasks)

    return {
        "title_field": title_field,
        "start_date_field": start_date_field,
        "start_date_picker": start_date_picker,
        "end_date_field": end_date_field,
        "end_date_picker": end_date_picker,
        "input_dialog": input_dialog,
        "fab": fab,
        "tasks_column": tasks_column
    }
