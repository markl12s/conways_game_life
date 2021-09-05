board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def check_cell(target_cell_x, target_cell_y):
    live_near = 0

    try:
        if board[target_cell_x - 1][target_cell_y - 1] == 1:
            live_near += 1
        if board[target_cell_x - 1][target_cell_y] == 1:
            live_near += 1
        if board[target_cell_x - 1][target_cell_y + 1] == 1:
            live_near += 1

        if board[target_cell_x][target_cell_y - 1] == 1:
            live_near += 1
        if board[target_cell_x][target_cell_y] == 1:
            live_near += 1
        if board[target_cell_x][target_cell_y + 1] == 1:
            live_near += 1

        if board[target_cell_x + 1][target_cell_y - 1] == 1:
            live_near += 1
        if board[target_cell_x + 1][target_cell_y] == 1:
            live_near += 1
        if board[target_cell_x + 1][target_cell_y + 1] == 1:
            live_near += 1

    #edge-cases
    except:
        #corners
        if target_cell_x == 0 and target_cell_y == 0:
            #checks
        elif target_cell_x == 0 and target_cell_y == -1:
            #checks
        elif target_cell_x == -1 and target_cell_y == 0:
            #checks
        elif target_cell_x == -1 and target_cell_y == -1:
            #checks

        #x is on top
        elif target_cell_x == 0:
            if target_cell_y != 0 or target_cell_y != -1:
                if board[target_cell_x][target_cell_y - 1] == 1:
                    live_near += 1
                if board[target_cell_x][target_cell_y] == 1:
                    live_near += 1
                if board[target_cell_x][target_cell_y + 1] == 1:
                    live_near += 1

                if board[target_cell_x + 1][target_cell_y - 1] == 1:
                    live_near += 1
                if board[target_cell_x + 1][target_cell_y] == 1:
                    live_near += 1
                if board[target_cell_x + 1][target_cell_y + 1] == 1:
                    live_near += 1

        #x is on bottom
        elif target_cell_x == -1:
            if target_cell_y != 0 or target_cell_y != -1:
                if board[target_cell_x - 1][target_cell_y - 1] == 1:
                    live_near += 1
                if board[target_cell_x - 1][target_cell_y] == 1:
                    live_near += 1
                if board[target_cell_x - 1][target_cell_y + 1] == 1:
                    live_near += 1

                if board[target_cell_x][target_cell_y - 1] == 1:
                    live_near += 1
                if board[target_cell_x][target_cell_y] == 1:
                    live_near += 1
                if board[target_cell_x][target_cell_y + 1] == 1:
                    live_near += 1

        #y is on left
        elif target_cell_y == 0:
            if target_cell_x != 0 or target_cell_x != -1:

        #y is on bottom


    finally:
        if board[target_cell_x][target_cell_y] == 0:
            if live_near == 3:
                live_or_dead.append(1)
            else:
                live_or_dead.append(0)
        elif board[target_cell_x][target_cell_y] == 1:
            if live_near == 2:
                live_or_dead.append(1)
            elif live_near == 3:
                live_or_dead.append(1)
            else:
                live_or_dead.append(0)

def turn_check():
    live_or_dead = []
    for x in range(10):
        for y in range(10):
            check_cell(target_cell_x, target_cell_y)

def change_states(target):
