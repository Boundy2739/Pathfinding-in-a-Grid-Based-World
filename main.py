import random
import time
import os
import sys
import heapq
sys.setrecursionlimit(1500)

def create_grid(entrance,previous,finish):
    grid = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,0,0,0,0,7,0,0,0,2,2,2,2],
    [2,2,0,0,0,0,0,2,2,0,0,0,2,0,0,0,2,2,2,2],
    [2,2,0,0,0,0,0,2,2,0,0,0,2,0,0,0,2,2,2,2],
    [2,2,0,0,0,0,0,2,2,2,2,0,2,0,0,0,2,2,2,2],
    [2,2,0,0,0,0,0,2,2,2,2,2,2,0,0,0,2,2,2,2],
    [2,2,0,0,0,0,0,2,2,2,2,2,2,0,0,0,2,2,2,2],
    [2,2,0,0,0,0,0,2,2,2,2,2,2,0,0,0,2,2,2,2],
    [2,2,0,0,0,0,0,2,2,2,2,2,2,2,0,0,2,2,2,2],
    [2,2,0,0,0,0,0,2,2,2,2,2,2,2,2,0,2,2,2,2],
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
    }
    #temporary starting line
    grid[entrance[0]][entrance[1]] = 1
    #temporary finish
    grid[finish[0]][finish[1]] = 5
    #grid = create_wall(grid)
    for rows in grid:
        print("".join([map.get(cell) for cell in rows]))
        
        
    return grid

def random_grid(entrance,previous,exit):
    grid = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    ]
    global map 
    map = {
        0 :" ",
        1 : "\033[44m \033[0m",
        3 : "\033[41m \033[0m",
        2 : '█',
        4 : "\033[46m \033[0m",
        5 : "\033[43m \033[0m",
    }
    create_spaces(grid,entrance,previous)
    grid[exit[0]][exit[1]] = 5
    for rows in grid:
        print("".join([map.get(cell) for cell in rows]))

    return grid

def dfs(entrance,current_grid,columns,finish,previous):
    
    while entrance[1] < columns - 1:
        nearby_cell = [current_grid [entrance[0] + 1][entrance[1]],current_grid [entrance[0] - 1][entrance[1]],current_grid [entrance[0]][entrance[1]+1],current_grid [entrance[0]][entrance[1]-1]]
        #this checks if theres is a free path both up and down picks a random path to follow
        if current_grid [entrance[0] + 1][entrance[1]] == 0 and current_grid[entrance[0] - 1][entrance[1]] == 0:
            pick_a_path_updown(current_grid,entrance)
            if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
        elif current_grid [entrance[0] + 1][entrance[1]] == 0 and current_grid[entrance[0]][entrance[1]+1] == 0:
            pick_a_path_rightdown(current_grid,entrance)
            if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
        elif current_grid [entrance[0]][entrance[1]-1] == 0 and current_grid[entrance[0]][entrance[1]+1] == 0:
            pick_a_path_leftright(current_grid,entrance)
            if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
        elif current_grid [entrance[0]][entrance[1]-1] == 0 and current_grid[entrance[0]-1][entrance[1]] == 0:
            pick_a_path_leftup(current_grid,entrance)
            if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
        elif current_grid [entrance[0]][entrance[1]-1] == 0 and current_grid[entrance[0]+1][entrance[1]] == 0:
            pick_a_path_leftdown(current_grid,entrance)
            if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
        elif current_grid [entrance[0]][entrance[1]+1] == 0 and current_grid[entrance[0]-1][entrance[1]] == 0:
            pick_a_path_rightup(current_grid,entrance)
            if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
        else:
                
            #moves right if there is space
                if nearby_cell[2] not in [2,1,3]: 
                   entrance = move_right(current_grid,entrance,finish,previous)
                #moves down if there is space
                elif nearby_cell[0] not in [2,1,3]:
                    entrance = move_down(current_grid,entrance,finish,previous)
                #moves up if there is space
                elif nearby_cell[1] not in [2,1,3]:
                    entrance = move_up(current_grid,entrance,finish,previous)
                #moves left if there is space
                elif nearby_cell[3] not in [2,1,3]: 
                    entrance = move_left(current_grid,entrance,finish,previous)
                
                
                
        if  current_grid [finish[0]][finish[1]] == 1:
                    print("Exit reached!!!")
                    return
def move_right(current_grid,entrance,finish,previous):
                    
                    previous_step = [entrance[0],entrance[1]]
                    previous.append(previous_step)
                    entrance[1] = entrance[1] + 1
                    current_grid = update_grid(current_grid,entrance)
                    if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
                    return backstep(current_grid,entrance,previous)
                          
def move_left(current_grid,entrance,finish,previous):
                    previous_step = [entrance[0],entrance[1]]
                    previous.append(previous_step)
                    entrance[1] = entrance[1] - 1
                    current_grid = update_grid(current_grid,entrance)                    
                    if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
                    return backstep(current_grid,entrance,previous)             
def move_up(current_grid,entrance,finish,previous):
                    previous_step = [entrance[0],entrance[1]]
                    previous.append(previous_step)
                    entrance[0] = entrance[0] - 1
                    current_grid = update_grid(current_grid,entrance)
                    if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
                    return backstep(current_grid,entrance,previous)                  
def move_down(current_grid,entrance,finish,previous):
    
                    previous_step = [entrance[0],entrance[1]]
                    previous.append(previous_step)
                    entrance[0] = entrance[0] + 1
                    current_grid = update_grid(current_grid,entrance)
                    if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
                    return backstep(current_grid,entrance,previous)
def pick_a_path_updown(current_grid,entrance):
    path = random.choice((1,2))
    previous_step = [entrance[0],entrance[1]]
    previous.append(previous_step)
    match path:
        case 1:
           entrance[0] = entrance[0] + 1
           current_grid = update_grid(current_grid,entrance)
        case 2:
            entrance[0] = entrance[0] - 1
            current_grid = update_grid(current_grid,entrance)
    return            
def pick_a_path_rightdown(current_grid,entrance):
    path = random.choice((1,2))
    previous_step = [entrance[0],entrance[1]]
    previous.append(previous_step)
    match path:
        case 1:
           entrance[0] = entrance[0] + 1
           current_grid = update_grid(current_grid,entrance)
        case 2:
            entrance[1] = entrance[1] + 1
            current_grid = update_grid(current_grid,entrance)
    return 
def pick_a_path_leftright(current_grid,entrance):
    path = random.choice((1 ,2))
    previous_step = [entrance[0],entrance[1]]
    previous.append(previous_step)
    match path:
        case 1:
           entrance[1] = entrance[1] - 1
           current_grid = update_grid(current_grid,entrance)
        case 2:
            entrance[1] = entrance[1] + 1
            current_grid = update_grid(current_grid,entrance)
    return 
def pick_a_path_rightup(current_grid,entrance):
    path = random.choice((1,2))
    previous_step = [entrance[0],entrance[1]]
    previous.append(previous_step)
    match path:
        case 1:
           entrance[0] = entrance[0] - 1
           current_grid = update_grid(current_grid,entrance)
        case 2:
            entrance[1] = entrance[1] + 1
            current_grid = update_grid(current_grid,entrance)
    return
def pick_a_path_leftdown(current_grid,entrance):
    path = random.choice((1,2))
    previous_step = [entrance[0],entrance[1]]
    previous.append(previous_step)
    match path:
        case 1:
           entrance[0] = entrance[0] + 1
           current_grid = update_grid(current_grid,entrance)
        case 2:
            entrance[1] = entrance[1] - 1
            current_grid = update_grid(current_grid,entrance)
    return
def pick_a_path_leftup(current_grid,entrance):
    path = random.choice((1,2))
    previous_step = [entrance[0],entrance[1]]
    previous.append(previous_step)
    match path:
        case 1:
           entrance[0] = entrance[0] - 1
           current_grid = update_grid(current_grid,entrance)
        case 2:
            entrance[1] = entrance[1] - 1
            current_grid = update_grid(current_grid,entrance)
    return




    

def update_grid(grid,entrance):
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    if grid[entrance[0]][entrance[1]] == 1:
          grid[entrance[0]][entrance[1]] = 3
    else:
          grid[entrance[0]][entrance[1]] = 1
    for rows in grid:
        print("".join([map.get(cell) for cell in rows]))
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    return grid

def right_space(grid,entrance,previous):
     
     
     if grid[entrance[0]][entrance[1] + 2] == 4: 
            previous_sp = [entrance[0],entrance[1]]
            previous.append(previous_sp)
            entrance[1] = entrance[1] + 1
            grid[entrance[0]][entrance[1]] = 0
            entrance[1] = entrance[1] + 1
            grid[entrance[0]][entrance[1]] = 0
            return entrance
     else:
        return backtrack(grid,entrance,previous)       
      
     
def left_space(grid,entrance,previous):
        
        if grid[entrance[0]][entrance[1]- 2] == 4:
                previous_sp = [entrance[0],entrance[1]]
                previous.append(previous_sp) 
                entrance[1] = entrance[1] - 1
                grid[entrance[0]][entrance[1]] = 0
                entrance[1] = entrance[1] - 1
                grid[entrance[0]][entrance[1]] = 0
                return entrance
        else:
            return backtrack(grid,entrance,previous)        
               
                
        
     
        
def up_space(grid,entrance,previous):
      if grid[entrance[0] - 2][entrance[1]] == 4:
        previous_sp = [entrance[0],entrance[1]]
        previous.append(previous_sp) 
        entrance[0] = entrance[0] - 1
        grid[entrance[0]][entrance[1]] = 0
        entrance[0] = entrance[0] - 1
        grid[entrance[0]][entrance[1]] = 0
        return entrance
      else:
        return backtrack(grid,entrance,previous)
          
def down_space(grid,entrance,previous):
     if grid[entrance[0] + 2][entrance[1]] == 4:
                previous_sp = [entrance[0],entrance[1]]
                previous.append(previous_sp) 
                entrance[0] = entrance[0] + 1
                grid[entrance[0]][entrance[1]] = 0
                entrance[0] = entrance[0] + 1
                grid[entrance[0]][entrance[1]] = 0
                return entrance
     else:
       return backtrack(grid,entrance,previous)
       
               
def backtrack(grid,entrance,previous):
      if grid[entrance[0]][entrance[1] - 2] !=4 and grid[entrance[0]+2][entrance[1]] !=4  and grid[entrance[0]-2][entrance[1]] !=4  and grid[entrance[0]][entrance[1]+2] !=4:
       entrance = previous[-1]
       previous.pop(-1)
       return backtrack(grid,entrance,previous)
       
         
      else:
        return entrance
def backstep(grid,entrance,previous):
     neighbours = [grid[entrance[0]][entrance[1] - 1],grid[entrance[0]][entrance[1] + 1],grid[entrance[0]-1][entrance[1]],grid[entrance[0]+1][entrance[1]]]
     if all(value != 0 for value in neighbours) and all(value != 5 for value in neighbours):
       entrance = previous[-1]
       previous.pop(-1)
       update_grid(grid,entrance) 
       return backstep(grid,entrance,previous)
     else:
          return entrance
                     
                
    
             
def create_spaces(grid,entrance,previous):
    
    for rows in grid:
         if any(cell == 4 for cell in rows):
            #time.sleep(0.1)
            os.system('cls' if os.name == 'nt' else 'clear')
            exit = [15,28]
            
            
            space = random.choice((1,2,3,4))
            match space:
                    case 1:
                        entrance = right_space(grid,entrance,previous)
                    case 2:
                        entrance = left_space(grid,entrance,previous)   
                    case 3:
                        entrance = up_space(grid,entrance,previous)      
                    case 4:
                        entrance = down_space(grid,entrance,previous)     
                
            #for rows in grid:
                #print("".join([map.get(cell) for cell in rows]))
            create_spaces(grid,entrance,previous)
    return grid

class aStar:
      def __init__(self,entrance,grid,finish):
            self.grid = grid
            self.rows = len(grid)
            self.columns = len(grid[0])
      
      class node:
        def __init__(self,cell,finish,g,grid):
                self.type = self.cell_type(grid[cell[0]][cell[1]])
                self.g = g+self.move_cost(self.type)
                self.h = self.heuristic(cell,finish)
                self.f = self.g + self.h
                self.cord = cell
                self.nearby = [[cell[0]+1,cell[1]],[cell[0]-1,cell[1]],[cell[0],cell[1]+1],[cell[0],cell[1]-1]]
                
        def heuristic(self,a,b):
            y1,x1 = a
            y2,x2 = b
            return abs(x1-x2) + abs(y1-y2)
        def gScore(self,a,b):
              y = abs(a[0]-b[0])
              x = abs(a[1]-b[1])
              return x + y
        def cell_type(self,cell):
              if cell == 0:
                    type = "empty"
              elif cell == 1:
                    type = "taken"
              elif cell == 2:
                    type = "wall"
              elif cell == 3:
                    type = "taken"
              elif cell == 5:
                    type = "exit"
              elif cell == 6:
                    type = "bush"
              elif cell == 7:
                    type = "water"
              return type
        def move_cost(self,type):
              if type == "empty" or type == "exit":
                    cost = 1
              elif type == "bush":
                    cost = 3
              elif type == "water":
                    cost = 6
              elif type == "taken":
                    cost = 0
              return cost
      
      def pathfinder(self,entrance,finish):
            all_cells = [(r, c) for r in range(self.rows) for c in range(self.columns)]
            startNode = self.node(entrance,finish,0,self.grid)
            currCell = self.node(entrance,finish,0,self.grid)
            open = []
            possibles = []
            closed = []
            open.append(startNode)
            steps = 0
            
            while True:
                  
                  if self.grid[finish[0]][finish[1]] == 1:
                     print(steps," taken")
                     return
                  
                  for cell in open:
                        if cell not in closed:
                            if cell.f < currCell.f or cell.f == currCell.f and cell.h < currCell.h:
                                if cell.type != "wall":
                                    currCell = cell            
                            elif cell.f == currCell.f and cell.h == currCell.h:
                                currCell = random.choice((cell,currCell))
                            
                            else:
                                best = min(open, key=lambda n: (n.f, n.h))
                                currCell = best
                                
                  update_grid(self.grid,currCell.cord)
                  steps += 1             
                  closed.append(currCell)
                  if currCell in open:
                    open.remove(currCell)
                  if startNode in open:
                    open.remove(startNode)
                  count = 0
                  for cells in currCell.nearby:
                        
                        if self.grid[cells[0]][cells[1]] in [0,5,6,7]:
                              print("free space")
                              pNode = self.node(cells,finish,currCell.g,self.grid)
                              open.append(pNode)
                              
                        
                           
                        
                              
                              
                        count += 1
                  
            return
              




previous = []
entrance = [2,2]
finish = [13,15]


current_grid = create_grid(entrance,previous,finish)
entrance = (2,2)
current_step = entrance
previous = []
columns = len(current_grid[0])
#move(entrance,current_grid,columns,finish,previous)
a = aStar(entrance,current_grid,finish)
a.pathfinder(entrance,finish)
print(a)


