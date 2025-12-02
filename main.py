import random
import time
import os
import sys
import heapq
sys.setrecursionlimit(1500)

def create_grid(entrance,finish,previous):
    grid = [
    [2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,2,0,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,2,0,2,2,2,2,2,2,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,2,0,2,2,2,2,2,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0],
    ]
    global map 
    map = {
        0 :" ",
        1 : "\033[44m \033[0m",
        3 : "\033[41m \033[0m",
        2 : '█',
        5 : "\033[43m \033[0m",
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

def move(entrance,current_grid,columns,finish,previous):
    
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
                
            for rows in grid:
                print("".join([map.get(cell) for cell in rows]))
            create_spaces(grid,entrance,previous)
    return grid

def a_star(entrance,current_step,finish,current_grid,previous):
      rows = len(current_grid)
      cols = len(current_grid[0])
      all_cells = [(r, c) for r in range(rows) for c in range(cols)]
       
      open = []
      closed = []
      heapq.heapify(open)
      cameFrom = {}
      #distance from current node to start
      gScore = {cell: ('inf') for cell in all_cells}
      gScore[entrance] = 0
    
      fScore = {cell: ('inf') for cell in all_cells}
      fScore[entrance] = gScore[entrance] + h(entrance,finish)
      heapq.heappush(open,(fScore[entrance],h(entrance,finish),gScore[entrance],entrance))

      while open:
            currG,currH,currF,currCell = heapq.heappop(open)
            nearby_cell = [current_grid [currCell[0] + 1][currCell[1]],current_grid [currCell[0] - 1][currCell[1]],current_grid [currCell[0]][currCell[1]+1],current_grid [currCell[0]][currCell[1]-1]]
            if currCell == finish:
                  print("ok")
                  break
            
            
            closed.append(currCell)

            for cell in nearby_cell:
                  if cell not in [1,2,3]:
                        if nearby_cell[0] == 0 :
                              neighbour = (currCell[0]+1,currCell[1])
                              newGscore = currG + distance(currCell,neighbour)
                              gScore[neighbour] = newGscore
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              fScore[neighbour]=newFscore
                              neighbourset =(newFscore,newHscore,newGscore,neighbour)
                              if neighbourset not in open:
                                heapq.heappush(open,(neighbourset))
                              print("ok")
                        if nearby_cell[1] == 0 :
                              neighbour = (currCell[0]-1,currCell[1])
                              newGscore = currG + distance(currCell,neighbour)
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              neighbourset =(newFscore,newHscore,newGscore,neighbour)
                              if neighbourset not in open:
                                heapq.heappush(open,(neighbourset))
                              print("ok")
                        if nearby_cell[2] == 0 :
                              neighbour = (currCell[0],currCell[1]+1)
                              newGscore = currG + distance(currCell,neighbour)
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              neighbourset =(newFscore,newHscore,newGscore,neighbour)
                              if neighbourset not in open:
                                heapq.heappush(open,(neighbourset))
                              print("ok")
                        if nearby_cell[3] == 0 :
                              neighbour = (currCell[0]+1,currCell[1]-1)
                              newGscore = currG + distance(currCell,neighbour)
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              neighbourset =(newFscore,newHscore,newGscore,neighbour)
                              if neighbourset not in open:
                                heapq.heappush(open,(neighbourset))
                              print("ok")
                        

      


      return     
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2) + abs(y1-y2)

def distance(cell1,cell2):
      dx = abs(cell1[1] - cell2[1])
      dy = abs(cell1[0] - cell2[0])
      return dx + dy
previous = []
entrance = [2,2]
finish = [12,46]
columns = 60

current_grid = random_grid(entrance,previous,finish)
entrance = (2,2)
current_step = entrance
previous = []
#move(entrance,current_grid,columns,finish,previous)
a = a_star(entrance,current_step,finish,current_grid,previous)

print(a)


