def create_grid(entrance,previous,finish):
    grid = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    ]
    global map 
    map = {
        0 :" ",
        1 : "\033[44m \033[0m",
        3 : "\033[41m \033[0m",
        2 : '█',
        5 : "\033[43m \033[0m",
        6 : "\033[102m \033[0m",
        7 : "\033[106m \033[0m",
        10 : "\033[45m \033[0m",
    }
    #temporary starting line
    grid[entrance[0]][entrance[1]] = 1
    #temporary finish
    grid[finish[0]][finish[1]] = 5
    #grid = create_wall(grid)
    for rows in grid:
        print("".join([map.get(cell) for cell in rows]))
        
        
    return grid


def editor(entrance, grid, finish):

    y, x = 2, 2  
    cursor = [y, x]

    
    prev = -1
    
    

    tile_edit = False
    while True:
        moved = False
        if keyboard.is_pressed("left"):
            if prev >= 0:
                 grid[y][x] = prev
            x -= 1
            moved = True

        elif keyboard.is_pressed("right"):
            if prev >= 0:
                 grid[y][x] = prev
            x += 1
            moved = True

        elif keyboard.is_pressed("up"):
            if prev >= 0:
                 grid[y][x] = prev
            y -= 1
            moved = True

        elif keyboard.is_pressed("down"):
            if prev >= 0:
                 grid[y][x] = prev
            y += 1
            moved = True
        elif keyboard.is_pressed("enter") and tile_edit == False:

            tile_edit = True
            edit_tile(grid,cursor)
            update_grid(grid,[y,x])
            prev = grid[y][x]
        elif keyboard.is_pressed("x") and tile_edit == False:

           return grid
            
        if tile_edit == True and not keyboard.is_pressed("enter"):
             tile_edit = False
        if moved:
            prev = grid[y][x]
            cursor[0], cursor[1] = y, x
            print(f"Cursor moved to {cursor}")
            grid[y][x] = 10
            update_grid(grid,cursor)
            time.sleep(0.15)   


def edit_tile(grid, cursor):
    y, x = cursor
    
    
    print("\n--- TILE EDITOR ---")
    print("\n--- Insert a value ---")
    print("2 = Wall")
    print("5 = maze exit tile")
    print("6 = Bush tile")
    print("7 = Water tile")
    print("0 = Clear tile")
    print("9 = Cancel")
    print("-------------------")

    while True:
        if keyboard.is_pressed("2"):
            print(f"Tile at {cursor} set to {2}")
            grid[y][x] = 2
            time.sleep(0.5)
            return 
        elif keyboard.is_pressed("5"):
            grid[y][x] = 5
            print(f"Tile at {cursor} set to {5}")
            time.sleep(0.5)
            return 
        elif keyboard.is_pressed("6"):
            grid[y][x] = 6
            print(f"Tile at {cursor} set to {6}")
            time.sleep(0.5)
            return 
        elif keyboard.is_pressed("7"):
            grid[y][x] = 7
            print(f"Tile at {cursor} set to {7}")
            time.sleep(0.5)
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