# choice options for the predefined pattern

def option_handler(event):
    global is_running, start_button, choice

    is_running = False
    start_button.configure(text='Start')

    selection = choice.get()

    if selection == 'glider':
        model.load_pattern(model.glider_pattern, 10, 10)

    elif selection == 'glider gun':
        model.load_pattern(model.glider_gun_pattern, 10, 10)

    elif selection == 'random':
        model.randomize(model.grid_model, model.width, model.height)

    update()
    
