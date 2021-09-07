"""
Conway's game of life, Mark Leard
v 1.1.1

last change: completed

next task: plan physical build
"""

#board initial state
board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#board_switching
board_swap = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#functions/architecture
def check_cell(target_cell_x, target_cell_y):
    live_cells_nearby = 0

    #corners
    if target_cell_x == 0 and target_cell_y == 0:
        live_cells_nearby = top_left_corner()
    elif target_cell_x == -1 and target_cell_y == 0:
        live_cells_nearby = bot_left_corner()
    elif target_cell_x == 0 and target_cell_y == -1:
        top_right_corner()
    elif target_cell_x == -1 and target_cell_y == -1:
        bot_right_corner()

    #middle cells
    elif target_cell_x != 0 and target_cell_x != -1:
        if target_cell_y != 0 and target_cell_y != -1:
            live_cells_nearby = add_row(target_cell_x - 1, target_cell_y)
            live_cells_nearby += add_sides(target_cell_x, target_cell_y)
            live_cells_nearby += add_row(target_cell_x + 1, target_cell_y)

    #check if cell is alive
    if board[target_cell_x][target_cell_y] == 0:
        if live_cells_nearby == 3:
            return 1
        else:
            return 0
    else:
        if live_cells_nearby == 2:
            return 1
        elif live_cells_nearby == 3:
            return 1
        else:
            return 0

def turn_check():
    live_or_dead = []
    for x in range(10):
        for y in range(10):
            dead_or_alive = check_cell(x, y)
            board_swap[x][y] = dead_or_alive

#checking cells nearby
def add_row(middle_x, middle_y):
    row = []

    row.append(board[(middle_x) % 10][(middle_y - 1) % 10])
    row.append(board[(middle_x) % 10][middle_y])
    row.append(board[(middle_x) % 10][(middle_y + 1) % 10])

    return sum(row)

def add_sides(middle_x, middle_y):
    row = []

    row.append(board[middle_x][middle_y - 1])
    row.append(board[middle_x][(middle_y + 1) % 10])

    return sum(row)

#corners
def top_left_corner():
    nearby_cells = []

    nearby_cells.append(board[-1][-1])
    nearby_cells.append(board[-1][0])
    nearby_cells.append(board[-1][1])

    nearby_cells.append(board[0][-1])
    nearby_cells.append(board[0][1])

    nearby_cells.append(board[1][-1])
    nearby_cells.append(board[1][0])
    nearby_cells.append(board[1][1])

    return sum(nearby_cells)

def bot_left_corner():
    nearby_cells = []

    nearby_cells.append(board[-2][-1])
    nearby_cells.append(board[-2][0])
    nearby_cells.append(board[-2][1])

    nearby_cells.append(board[-1][-1])
    nearby_cells.append(board[-1][1])

    nearby_cells.append(board[0][-1])
    nearby_cells.append(board[0][0])
    nearby_cells.append(board[0][1])

    return sum(nearby_cells)

def top_right_corner():
    nearby_cells = []

    nearby_cells.append(board[-1][0])
    nearby_cells.append(board[0][0])
    nearby_cells.append(board[1][0])

    nearby_cells.append(board[1][-1])
    nearby_cells.append(board[-1][-1])

    nearby_cells.append(board[-1][-2])
    nearby_cells.append(board[0][-2])
    nearby_cells.append(board[1][-2])

    return sum(nearby_cells)

def bot_right_corner():
    nearby_cells = []

    nearby_cells.append(board[-1][0])
    nearby_cells.append(board[0][0])
    nearby_cells.append(board[1][0])

    nearby_cells.append(board[-1][-1])
    nearby_cells.append(board[1][-1])

    nearby_cells.append(board[-1][-2])
    nearby_cells.append(board[0][-2])
    nearby_cells.append(board[1][-2])

    return sum(nearby_cells)

#execution
print(board)

while True:
    turn_check()
    board = board_swap
    print(board)
