from core import data

def cancel_dialog_button(page):
    def handler(e):
        if page.overlay:
            page.overlay[0].open = False
        page.update()
    return handler

def add_dialog_button(page, input_field, tasks_column, layout):
    def handler(e):
        task_title = input_field.value
        start_date = "2026-12-25"
        end_date = "2026-12-31"
        data.add_task(task_title, start_date, end_date)

        layout.render_tasks(page, data.get_tasks(), tasks_column)

        if page.overlay:
            page.overlay[0].open = False
        input_field.value = ""
        page.update()
    return handler

def open_dialog_button(page):
    def handler(e):
        if page.overlay:
            page.overlay[0].open = True
        page.update()
    return handler
