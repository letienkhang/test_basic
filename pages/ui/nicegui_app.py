from nicegui import ui
import subprocess
import threading
import queue
import time

environments = {
    'Dev': 'https://dev.yody.io/',
    'UAT': 'https://uat.yody.io/',
    'Prod': 'https://beta.yody.vn/',
    'Dev - Unicorn': 'https://unicorn-dev.yody.io/',
    'UAT - Unicorn': 'https://unicorn-uat.yody.io/'
}

tasks = {
    'Task Canonical': '/Users/kanglee/PycharmProjects/pythonProject5/pages/canonical/canonical_page.py',
    'Task Index - Follow': '/Users/kanglee/PycharmProjects/pythonProject5/pages/sitemap/sitemap.py',
    'Task Checkout': '/Users/kanglee/PycharmProjects/pythonProject5/pages/checkout_basic/test.py',
    'Checkout Link': '/Users/kanglee/PycharmProjects/pythonProject5/pages/checkou_by_link/main.py',
    'Task Same price': '/Users/kanglee/PycharmProjects/pythonProject5/pages/same_price/test.py',
    'Promotion - Order': '/Users/kanglee/PycharmProjects/pythonProject5/pages/promotion_order/test.py'
}

selected_environment = {'value': list(environments.keys())[0]}
selected_task = {'value': list(tasks.keys())[0]}
num_browsers = {'value': 1}

task_queue = queue.Queue()


def run_task(base_url, task_script, num_browsers):
    for _ in range(num_browsers):
        full_script_path = task_script
        subprocess.Popen(['python', full_script_path, base_url])
        time.sleep(1)


def on_environment_change(event):
    selected_environment['value'] = event.value


def on_task_change(event):
    selected_task['value'] = event.value


def on_browser_selection_change(event):
    try:
        num_browsers['value'] = int(event.value)
    except ValueError:
        ui.notify('Please select a valid number.')


def on_run():
    try:
        if num_browsers['value'] > 0:
            env_name = selected_environment['value']
            base_url = environments[env_name]
            task_name = selected_task['value']
            task_script = tasks[task_name]
            task_queue.put((base_url, task_script, num_browsers['value']))
            ui.notify('Starting tasks...')
            task_processor_thread = threading.Thread(target=process_task_queue)
            task_processor_thread.start()
        else:
            ui.notify('Please enter a valid number greater than 0.')
    except ValueError:
        ui.notify('Please enter a valid number.')


def process_task_queue():
    while True:
        try:
            base_url, task_script, num_browsers = task_queue.get(timeout=1)
            run_task(base_url, task_script, num_browsers)
        except queue.Empty:
            continue
        except Exception as e:
            print(f"Error processing task queue: {e}")


with ui.grid(columns=2):
    ui.label('Environment:').classes('h-[70px] flex items-center justify-center').style('justify-self: start;')
    ui.select([env for env in environments.keys()], value=selected_environment['value'],
              on_change=on_environment_change).classes('h-[70px]')

    ui.label('Task:').classes('h-[70px] flex items-center justify-center').style('justify-self: start;')
    ui.select([task for task in tasks.keys()], value=selected_task['value'], on_change=on_task_change).classes(
        'h-[70px]')

    ui.label('Number of Browsers:').classes('h-[70px] flex items-center justify-center').style('justify-self: start;')
    ui.select(['1', '2', '3', '4', '5'], value='1', on_change=on_browser_selection_change).classes('h-[70px]')

ui.button('Run', icon='play_arrow', on_click=on_run).classes('mt-4 ml-4').props('elevated')

ui.run()
