#the code currently changes all the 0 in the rows into a 1 until it reaches a 5 which is the finish line for the time
import random
import time
import os

def create_grid(entrance,finish,wall):
    grid = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2,2],
    [0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2],
    [2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,2,2,2,2,2],
    [2,0,2,2,2,2,2,2,2,0,2,2,2,2,0,0,0,0,0,2],
    [2,0,2,2,2,2,2,2,2,0,2,2,2,2,2,2,2,0,0,2],
    [2,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,2],
    [2,2,2,2,2,0,2,0,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,2,0,0],
    [2,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,2,0,0],
    [2,2,2,2,0,2,2,2,2,2,2,2,2,2,0,0,0,2,0,0],
    [2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0],
    ]
    
    #temporary starting line
    grid[entrance[0]][entrance[1]] = 1
    #temporary finish
    grid[finish[0]][finish[1]] = 5
    #grid = create_wall(grid)
    for rows in grid:
        print("".join([' ' if cell == 0 else  '█' if cell == 2 else "\033[43m \033[0m" for cell in rows]))
        
        
    return grid
def move(entrance,current_grid,rows,columns,finish):
    while entrance[1] < columns - 1:
        #moves left if there is space
        while current_grid[entrance[0]][entrance[1] + 1] != 2 and current_grid[entrance[0]][entrance[1] + 1] != 1: 
            entrance[1] = entrance[1] + 1
            current_grid = update_grid(current_grid,entrance)
        #moves down if there is space
        while current_grid [entrance[0] + 1][entrance[1]] != 2 and current_grid [entrance[0] + 1][entrance[1]] != 1:
            entrance[0] = entrance[0] + 1
            current_grid = update_grid(current_grid,entrance)
        #moves up if there is space
        while current_grid [entrance[0] - 1][entrance[1]] != 2 and current_grid [entrance[0] - 1][entrance[1]] != 1:
            entrance[0] = entrance[0] - 1
            current_grid = update_grid(current_grid,entrance)
        #moves right if there is space
        while current_grid[entrance[0]][entrance[1] - 1] != 2 and current_grid[entrance[0]][entrance[1] - 1] != 1: 
            entrance[1] = entrance[1] - 1
            current_grid = update_grid(current_grid,entrance)
        
        
        if entrance [1] == columns - 1:
            entrance [1] = 0
            if entrance[0] < rows:
                entrance [0] += 1
            current_grid = update_grid(current_grid,entrance)
        if  current_grid [finish[0]][finish[1]] == 1:
            print("Over")
            return
            
    
    

def update_grid(grid,entrance):
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    grid[entrance[0]][entrance[1]] = 1
    for rows in grid:
        print("".join([' ' if cell == 0 else  '█' if cell == 2 else "\033[41m \033[0m" for cell in rows]))
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    return grid
def create_wall(grid):
    for i in range (19):
        rand_wall = random.randrange(0,19)
        if grid[0][rand_wall] == 0:
            grid[0][rand_wall] = 2
        else:
            print("space taken!!")

    for i in range (19):
        rand_wall = random.randrange(0,19)
        if grid[1][rand_wall] == 0:
            grid[1][rand_wall] = 2
        else:
            print("space taken!!")
    for i in range (19):
        rand_wall = random.randrange(0,19)
        if grid[2][rand_wall] == 0:
            grid[2][rand_wall] = 2
        else:
            print("space taken!!")
    for i in range (19):
        rand_wall = random.randrange(0,19)
        if grid[3][rand_wall] == 0:
            grid[3][rand_wall] = 2
        else:
            print("space taken!!")
    return grid

entrance = [1,0]
finish = [14,4]
wall = [0,1]
rows = 3
columns = 20

current_grid = create_grid(entrance,finish,wall)
new_point = move(entrance,current_grid,rows,columns,finish)


