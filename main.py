import random
import time
import os

def create_grid(entrance,finish,wall):
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
    [0,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,0,0],
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

def random_grid(entrance,previous):
    grid = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,4,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
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
    for rows in grid:
        print("".join([map.get(cell) for cell in rows]))

    return grid

def move(entrance,current_grid,rows,columns,finish,previous):
    while entrance[1] < columns - 1:
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
                if current_grid[entrance[0]][entrance[1] + 1] != 2 and current_grid[entrance[0]][entrance[1] + 1] != 1 and current_grid[entrance[0]][entrance[1] + 1] != 3: 
                   move_right(current_grid,entrance,finish)
                #moves down if there is space
                elif current_grid [entrance[0] + 1][entrance[1]] != 2 and current_grid [entrance[0] + 1][entrance[1]] != 1 and current_grid[entrance[0]+1][entrance[1]] != 3:
                    move_down(current_grid,entrance,finish)
                #moves up if there is space
                elif current_grid [entrance[0] - 1][entrance[1]] != 2 and current_grid [entrance[0] - 1][entrance[1]] != 1:
                    move_up(current_grid,entrance,finish)
                #moves left if there is space
                elif current_grid[entrance[0]][entrance[1] - 1] != 2 and current_grid[entrance[0]][entrance[1] - 1] != 1: 
                    move_left(current_grid,entrance,finish)
                
                
                if entrance [1] == columns - 1:
                    entrance [1] = 0
                    if entrance[0] < rows:
                        entrance [0] += 1
                    current_grid = update_grid(current_grid,entrance)
                if  current_grid [finish[0]][finish[1]] == 1:
                    print("Exit reached!!!")
                    return
def move_right(current_grid,entrance,finish):
    
                    entrance[1] = entrance[1] + 1
                    current_grid = update_grid(current_grid,entrance)
                    #if current_grid [entrance[0] + 1][entrance[1]] != 2 and current_grid[entrance[0] - 1][entrance[1]] != 2:
                        #pick_a_path(current_grid,entrance)
                    if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
                    if current_grid[entrance[0]][entrance[1] + 1] == 2 and current_grid[entrance[0]+1][entrance[1]] == 2 and current_grid[entrance[0]-1][entrance[1]] == 2:
                          back_left(current_grid,entrance,finish) 
def move_left(current_grid,entrance,finish):
    
                    entrance[1] = entrance[1] - 1
                    current_grid = update_grid(current_grid,entrance)
                    if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
                    back_right(current_grid,entrance,finish)             
def move_up(current_grid,entrance,finish):
    
                    entrance[0] = entrance[0] - 1
                    current_grid = update_grid(current_grid,entrance)
                    if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
                    back_down(current_grid,entrance,finish)
def move_down(current_grid,entrance,finish):
    
                    entrance[0] = entrance[0] + 1
                    current_grid = update_grid(current_grid,entrance)
                    if  current_grid [finish[0]][finish[1]] == 1:
                        print("Exit reached!!!")
                        return
                    if current_grid[entrance[0]][entrance[1] + 1] != 0 and current_grid[entrance[0]+1][entrance[1]] != 0 and current_grid[entrance[0]][entrance[1]-1] != 0:
                        back_up(current_grid,entrance,finish)
def pick_a_path_updown(current_grid,entrance):
    path = random.choice((1,2))
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
    match path:
        case 1:
           entrance[0] = entrance[0] - 1
           current_grid = update_grid(current_grid,entrance)
        case 2:
            entrance[1] = entrance[1] - 1
            current_grid = update_grid(current_grid,entrance)
    return

def back_left(current_grid,entrance,finish):
      if current_grid[entrance[0]][entrance[1] + 1] !=0 and current_grid[entrance[0]+1][entrance[1]] !=0  and current_grid[entrance[0]-1][entrance[1]] !=0 :
        entrance[1] = entrance[1] - 1
        current_grid = update_grid(current_grid,entrance)
        back_left(current_grid,entrance,finish) 
      else:
        return
def back_down(current_grid,entrance,finish):
      if current_grid[entrance[0]][entrance[1] + 1] !=0 and current_grid[entrance[0]-1][entrance[1]] !=0  and current_grid[entrance[0]][entrance[1]-1] !=0 :
        entrance[0] = entrance[0] + 1
        current_grid = update_grid(current_grid,entrance)
        back_down(current_grid,entrance,finish) 
      else:
        return
def back_right(current_grid,entrance,finish):
      if current_grid[entrance[0]][entrance[1] - 1] !=0 and current_grid[entrance[0]+1][entrance[1]] !=0  and current_grid[entrance[0]-1][entrance[1]] !=0  :
        entrance[1] = entrance[1] + 1
        current_grid = update_grid(current_grid,entrance)
        back_right(current_grid,entrance,finish) 
      else:
        return
def back_up(current_grid,entrance,finish):
      neighbours = [current_grid[entrance[0]][entrance[1]+1],current_grid[entrance[0]][entrance[1]-1],current_grid[entrance[0]+1][entrance[1]]]
      if all(value != 0 for value in neighbours) and not any (value == 5 for value in neighbours):
        if current_grid[entrance[0]-1][entrance[1]] != 2:
            entrance[0] = entrance[0] - 1
        else:
             if current_grid[entrance[0]][entrance[1] + 1] == 1:
                  entrance[1] = entrance[1] + 1
                  current_grid = update_grid(current_grid,entrance)
             return
        current_grid = update_grid(current_grid,entrance)
        back_up(current_grid,entrance,finish) 
      
      else:
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
     if all(value != 0 for value in neighbours):
       entrance = previous[-1]
       previous.pop(-1)
          
       return backstep(grid,entrance,previous)
     else:
          return entrance
                     
                
    
             
def create_spaces(grid,entrance,previous):
    
    for rows in grid:
         if any(cell == 4 for cell in rows):
            time.sleep(0.01)
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
    

previous = []
entrance = [2,2]
finish = [19,11]
rows = 3
columns = 20

current_grid = random_grid(entrance,previous)
entrance = [2,2]
previous = []
new_point = move(entrance,current_grid,rows,columns,finish,previous)


