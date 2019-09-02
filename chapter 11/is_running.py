# this the code to change the start (set is_running to True) button to pause (set is_running to False).

is_running = False

global  is_running, start_button

if is_running:
    is_running = False
    start_button.configure(text='Start')
else:
    is_running = True
    start_button.configure(text='Pause')
    update()
