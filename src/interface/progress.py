from datetime import date
import flet as ft


def calculate_progress(start_date, end_date):
    today = date.today()
    total_days = (end_date - start_date).days
    elapsed_days = (today - start_date).days

    if total_days == 0:
        return 100.0

    percentage = (elapsed_days / total_days) * 100
    return max(0, min(100, percentage))

def get_progress_color(percentage):
    if percentage <= 30:
        return ft.Colors.GREEN
    elif percentage <= 45:
        return ft.Colors.YELLOW
    elif percentage <= 80:
        return ft.Colors.ORANGE
    else:
        return ft.Colors.RED


def build_progress_bar(start_date, end_date):
    percentage = calculate_progress(start_date, end_date)
    color = get_progress_color(percentage)

    bar_width = 300
    dot_position = (bar_width - 10) * (percentage / 100)

    bar = ft.Row([
        ft.Text("Started", size=10),
        ft.Stack([
            ft.Container(
                width=bar_width,
                height=4,
                bgcolor=ft.Colors.GREY_300,
                border_radius=3,
                top=8
            ),
            ft.Container(
                width=dot_position,
                height=4,
                bgcolor=color,
                border_radius=3,
                top=8
            ),
            ft.Container(
                width=12,
                height=12,
                bgcolor=color,
                border_radius=6,
                left=dot_position
            )
        ], width=bar_width, height=20),
        ft.Text("Due", size=10)
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    return bar
