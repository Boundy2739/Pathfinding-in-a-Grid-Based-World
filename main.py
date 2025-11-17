#the code currently changes all the 0 in the rows into a 1 until it reaches a 5 which is the finish line for the time
import random

def create_grid(start,finish,wall):
    grid = [
    [0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2,2],
    [0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,0,0,0,0,2,0,2,2,2,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    
    #temporary starting line
    grid[start[0]][start[1]] = 1
    #temporary finish
    grid[finish[0]][finish[1]] = 5
    #grid = create_wall(grid)
    for rows in grid:
        print("".join([' ' if cell == 0 else  '█' if cell == 2 else '?' for cell in rows]))
        
        
    return grid
def move(start,current_grid,rows,columns,finish):
    while start[1] < columns - 1:
        if current_grid[start[0]][start[1] + 1] != 2: 
            start[1] = start[1] + 1
            current_grid = update_grid(current_grid,start)
        elif start [0] != 2 and start [0] != 1:
            start [0] += 1
            current_grid = update_grid(current_grid,start)
            
        elif start[0] - 1 != 2 and start [0] == 1:
            start [0] -= 1
            current_grid = update_grid(current_grid,start)

        if start [1] == columns - 1:
            start [1] = 0
            if start[0] < rows:
                start [0] += 1
            current_grid = update_grid(current_grid,start)
        if  current_grid [finish[0]][finish[1]] == 1:
            print("Over")
            return
            
    print (start[1])
    

def update_grid(grid,start):
    grid[start[0]][start[1]] = 1
    for rows in grid:
        print("".join([' ' if cell == 0 else  '█' if cell == 2 else '?' for cell in rows]))
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

start = [0,0]
finish = [3,19]
wall = [0,1]
rows = 3
columns = 20

current_grid = create_grid(start,finish,wall)
new_point = move(start,current_grid,rows,columns,finish)

