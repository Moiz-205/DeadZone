tasks = []

def add_task(title, start_date, end_date):
    task = {
        "title": title,
        "start_date": start_date,
        "end_date": end_date
    }
    tasks.append(task)
    return task

def get_tasks():
    return tasks
