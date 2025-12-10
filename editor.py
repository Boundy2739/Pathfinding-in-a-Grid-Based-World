import keyboard
import time
import os
global markers 
markers = {
        0 :" ",
        1 : "\033[44m \033[0m",
        3 : "\033[41m \033[0m",
        2 : '█',
        5 : "\033[43m \033[0m",
        6 : "\033[102m \033[0m",
        7 : "\033[106m \033[0m",
        10 : "\033[45m \033[0m",
        11: "\033[103m \033[0m",
    }
def create_grid(entrance,previous,finish):
    grid = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    ]
    
    #temporary starting line
    grid[entrance[0]][entrance[1]] = 1
    #temporary finish
    grid[finish[0]][finish[1]] = 5
    #grid = create_wall(grid)
    for rows in grid:
        print("".join([markers.get(cell) for cell in rows]))
        
    print("")
    print("Use the arrow keys to move around\n")
    print("Press enter to edit the current tile\n")
    print("Press x to exit the grid editor\n")   
    return grid


def editor(entrance, grid, finish):

    y, x = 2, 2  
    cursor = [y, x]
    prev = -1
    prev_entrance = [2,2]
    prev_exit = finish
    

    tile_edit = False
    while True:
        moved = False
        if keyboard.is_pressed("left") and tile_edit == False:
            if prev >= 0:
                 grid[y][x] = prev
            if x > 2:
                x -= 1
            moved = True

        elif keyboard.is_pressed("right") and tile_edit == False:
            if prev >= 0:
                 grid[y][x] = prev
            if x < len(grid[0]) - 3:
                x += 1
            moved = True

        elif keyboard.is_pressed("up") and tile_edit == False:
            if prev >= 0:
                 grid[y][x] = prev
            if y > 2:
                y -= 1
            moved = True

        elif keyboard.is_pressed("down") and tile_edit == False:
            if prev >= 0:
                 grid[y][x] = prev
            if y < len(grid) - 3:
                y += 1
            moved = True
        elif keyboard.is_pressed("enter") and tile_edit == False:

            tile_edit = True
            new_cell = edit_tile(grid,cursor,prev_entrance,prev_exit)
            prev = grid[y][x]
            if new_cell == 1:
                prev_entrance = [y,x]
            elif new_cell == 5:
                prev_exit = [y,x]
            update_grid(grid,[y,x])
        elif keyboard.is_pressed("x") and tile_edit == False:
           tile_edit = True
           if grid[y][x] == 10:
               grid[y][x] = 0
           print("exiting edit mode")
           return prev_entrance,prev_exit,grid
            
        if tile_edit == True and not keyboard.is_pressed("enter"):
             tile_edit = False
        if moved:
            prev = grid[y][x]
            cursor[0], cursor[1] = y, x
            grid[y][x] = 10
            update_grid(grid,cursor)
            print(f"Cursor moved to tile {cursor}")
            time.sleep(0.15)   


def edit_tile(grid, cursor,prev_entrance,prev_exit):
    y, x = cursor
    
    
    print("\n--- TILE EDITOR ---")
    print("\n--- Insert a value ---")
    print("1 = Entrance")
    print("2 = Wall")
    print("5 = maze exit tile")
    print("6 = Bush tile")
    print("7 = Water tile")
    print("0 = Clear tile")
    print("9 = Cancel")
    print("-------------------")

    while True:
        if keyboard.is_pressed("0"):
            print(f"Tile at {cursor} set to clear")
            grid[y][x] = 0
            
            return
        elif keyboard.is_pressed("1"):
            print(f"Tile at {cursor} set to entrance")
            grid[prev_entrance[0]][prev_entrance[1]] = 0
            grid[y][x] = 11
            
            return 1
        if keyboard.is_pressed("2"):
            print(f"Tile at {cursor} set to wall")
            grid[y][x] = 2
            
            return 
        elif keyboard.is_pressed("5"):
            grid[prev_exit[0]][prev_exit[1]] = 0
            grid[y][x] = 5
            print(f"Tile at {cursor} set to exit")
            
            return 5
        elif keyboard.is_pressed("6"):
            grid[y][x] = 6
            print(f"Tile at {cursor} set to bush")
            time.sleep(0.1)
            return 
        elif keyboard.is_pressed("7"):
            grid[y][x] = 7
            print(f"Tile at {cursor} set to river")
            
            return 
        elif keyboard.is_pressed("9"):
            
            print("canceled")
            time.sleep(1)
            return

     
def cursor_position(grid, cursor):
    os.system('cls' if os.name == 'nt' else 'clear')
    cy, cx = cursor

    for y, row in enumerate(grid):
        line = ""
        for x, cell in enumerate(row):
            if y == cy and x == cx:
                line += f"\033[43m{map.get(cell)}\033[0m"
            else:
                line += f" {map.get(cell)} "
        print(line)

    print("\n" * 3) 

def update_grid(grid,entrance):
    
    os.system('cls' if os.name == 'nt' else 'clear')
    for rows in grid:
        print("".join([markers.get(cell) for cell in rows]))
    print("")
    print("Use the arrow keys to move around\n")
    print("Press enter to edit the current tile\n")
    print("Press x to exit the grid editor\n")
    return grid