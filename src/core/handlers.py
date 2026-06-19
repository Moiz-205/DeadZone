from datetime import datetime
from core import data

def cancel_dialog_button(page):
    def handler(e):
        if page.overlay:
            page.overlay[0].open = False
        page.update()
    return handler

def add_dialog_button(page,
    title_field,
    start_date_field,
    end_date_field,
    tasks_column,
    layout):
    def handler(e):
        task_title = title_field.value
        start_date_str = start_date_field.value
        end_date_str = end_date_field.value

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format.")
            return

        data.add_task(task_title, start_date, end_date)
        layout.render_tasks(page, data.get_tasks(), tasks_column)

        if page.overlay:
            page.overlay[0].open = False
        title_field.value = ""
        start_date_field.value = ""
        end_date_field.value = ""
        page.update()
    return handler

def open_dialog_button(page):
    def handler(e):
        if page.overlay:
            page.overlay[0].open = True
        page.update()
    return handler
