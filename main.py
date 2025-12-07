import random
import time
import os
import sys
import heapq
import keyboard

sys.setrecursionlimit(1500)

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


    

def update_grid(grid,entrance):
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    if grid[entrance[0]][entrance[1]] == 1:
          grid[entrance[0]][entrance[1]] = 3
    elif grid[entrance[0]][entrance[1]] == 0:
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
        def __init__(self,cell,finish,grid):
                self.type = self.cell_type(grid[cell[0]][cell[1]])
                self.g = float('inf')
                self.h = self.heuristic(cell,finish)
                self.f = float('inf')
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
                    return float (1)
              elif cell == 1:
                    type = "taken"
                    return float(0)
              elif cell == 2:
                    type = "wall"
                    return 999
              elif cell == 3:
                    type = "taken"
                    return float(0)
              elif cell == 5:
                    type = "exit"
                    return float(1)
              elif cell == 6:
                    type = "bush"
                    return float(3)
              elif cell == 7:
                    type = "water"
                    return float(6)
              
      
      def pathfinder(self, entrance, finish):

        open_list = []
        open_set = set()
        closed_set = set()

        nodes = {}

        def get_node(c):
            if tuple(c) not in nodes:
                nodes[tuple(c)] = self.node(c, finish, self.grid)
            return nodes[tuple(c)]

        start = get_node(entrance)
        start.g = 0
        start.f = start.h
        counter = 0

        heapq.heappush(open_list, (start.f, start.h, counter, start))
        open_set.add(start)

        while open_list:

            f, h, _, current = heapq.heappop(open_list)
            open_set.remove(current)
            closed_set.add(current)

            if current.cord == finish:
                return True    # or reconstruct path

            for n in current.nearby:
                # skip walls
                if self.grid[n[0]][n[1]] not in (0,5,6,7):
                    continue

                neighbor = get_node(n)

                if neighbor in closed_set:
                    continue

                tentative_g = current.g + neighbor.type

                if tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.f = tentative_g + neighbor.h
                
                    counter += 1

                    # if not in open_list, push it
                    if neighbor not in open_set:
                        heapq.heappush(open_list, (neighbor.f, neighbor.h, counter, neighbor))
                        open_set.add(neighbor)
            update_grid(self.grid,current.cord) 

last_enter_time = 0


def editor(entrance, grid, finish):

    y, x = 2, 2  
    cursor = [y, x]

    

    
    

    tile_edit = False
    while True:
        moved = False
        
        if keyboard.is_pressed("left"):
            x -= 1
            moved = True

        elif keyboard.is_pressed("right"):
            x += 1
            moved = True

        elif keyboard.is_pressed("up"):
            y -= 1
            moved = True

        elif keyboard.is_pressed("down"):
            y += 1
            moved = True
        elif keyboard.is_pressed("enter") and tile_edit == False:

            tile_edit = True
            edit_tile(grid,cursor)
            update_grid(grid,[y,x])
        elif keyboard.is_pressed("x") and tile_edit == False:

           return grid
            
        if tile_edit == True and not keyboard.is_pressed("enter"):
             tile_edit = False
        if moved:
            cursor[0], cursor[1] = y, x
            print(f"Cursor moved to {cursor}")
            time.sleep(0.15)   


def edit_tile(grid, cursor):
    y, x = cursor
    input()
    while True:
        print("\n--- TILE EDITOR ---")
        print("\n--- Insert a value ---")
        print("2 = Wall")
        print("5 = maze exit tile")
        print("6 = Bush tile")
        print("7 = Water tile")
        print("0 = Clear tile")
        print("9 = Cancel")
        print("-------------------")

        value = input("> ")

        try:
            value = int(value)
        except ValueError:
            print("Please enter a number.")
            continue

        if value in [0, 2,5,6,7]:
            grid[y][x] = value
            print(f"Tile at {cursor} set to {value}")
            return value

        elif value == 9:
            print("Canceled.")
            time.sleep(1)
            return

        else:
            print("Invalid option.")
     

previous = []
entrance = [2,2]
finish = [10,15]


current_grid = create_grid(entrance,previous,finish)
entrance = (2,2)
editor(entrance,current_grid,finish)
current_step = entrance
previous = []
columns = len(current_grid[0])
#move(entrance,current_grid,columns,finish,previous)
a = aStar(entrance,current_grid,finish)
a.pathfinder(entrance,finish)
print(a)


