clear_button.bind('<Button-1>', clear_handler)

def clear_handler(event):
    global is_running, start_button

    is_running = False
    for i in range(0, model.height):
        for j in range(0, model.width):
            model.grid_model[i][j] = 0
    start_button.configure(text='Start')
    update()
