# Game of life, will be built on MVC
# M is for model and is stored as model.py
# V is for view and is stored as view.py
# C is for controller and is stored as controller.py
# we will compile the controller code

def update():
    global grid_view

    grid_view.delete(ALL)
    model.next_gen()

    for i in range(0, model.height):
        for j in range(0, model.width):
            if model.grid_model[i][j] == 1:
                draw_cell(i, j, 'black')

def draw_cell(row, col, color):
    global grid_view, cell_size

    if color == black:
        outline = 'grey'
    else:
        outline = 'white'

    grid_view.create_rectangle(row*cell_size, col*cell_size, row*cell_size+cell_size, col*cell_size+cell_size, fill=color, outline=outline)
    
