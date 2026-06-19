import flet as ft
from datetime import datetime

def create_date_picker_control():
    return ft.DatePicker(
        first_date=datetime(2020, 1, 1),
        last_date=datetime(2030, 12, 31)
    )
