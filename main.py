#the code currently changes all the 0 in the rows into a 1 until it reaches a 5 which is the finish line for the time
def create_grid(start,finish):
    grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    
    #temporary starting line
    grid[start[0]][start[1]] = 1
    #temporary finish
    grid[finish[0]][finish[1]] = 5
    for rows in grid:
        for elements in rows:
            print(elements, end=" ")
        print()
    return grid
def move(start,current_grid,rows,columns,finish):
    while start[1] < columns - 1:
        start[1] = start[1] + 1
        current_grid = update_grid(current_grid,start)
        if start [1] == columns - 1:
            start [1] = 0
            if start[0] != rows - 1 :
                start [0] += 1
            current_grid = update_grid(current_grid,start)
        if  current_grid [finish[0]][finish[1]] == 1:
            print("Over")
            return
            
    print (start[1])
    

def update_grid(grid,start):
    grid[start[0]][start[1]] = 1
    for rows in grid:
        for elements in rows:
            print(elements, end=" ")
        print()
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    return grid

start = [5,8]
finish = [9,15]

rows = 10
columns = 20
current_grid = create_grid(start,finish)
new_point = move(start,current_grid,rows,columns,finish)

