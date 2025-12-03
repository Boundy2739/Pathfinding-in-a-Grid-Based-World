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
def pick_a_path_leftup(current_grid,entrance)