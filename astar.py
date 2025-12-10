import heapq
import time
import os
global markers 
markers = {
        0 :" ",
        1 : "\033[44m \033[0m", #marker for cells visited
        3 : "\033[41m \033[0m", #marker for the best path found
        2 : '█', #marker for the walls
        5 : "\033[43m \033[0m", #marker for the exit
        6 : "\033[102m \033[0m", #marker for the bushes
        7 : "\033[106m \033[0m", #marker for the rivers
        10 : "\033[45m \033[0m", #marker for the purple cursor in edit mode
        11: "\033[48;5;208m \033[0m", #marker for the start cell
    }
def update_grid(grid,entrance):
   
    #time.sleep(0.1)
    #os.system('cls' if os.name == 'nt' else 'clear')
    for rows in grid:
        print("".join([markers.get(cell) for cell in rows]))
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    return grid

class aStar:
      def __init__(self,entrance,grid,finish):
            self.grid = grid
            self.rows = len(grid)
            self.columns = len(grid[0])
      
      class node:
        def __init__(self,cell,finish,grid):
                y, x = cell
                fy, fx = finish
                cell_value = grid[y][x]
                if cell_value == 0: self.type = 1       # empty
                elif cell_value == 1: self.type = 0     # taken
                elif cell_value == 2: self.type = 999   # wall
                elif cell_value == 3: self.type = 0     
                elif cell_value == 5: self.type = 1     #exit
                elif cell_value == 6: self.type = 3     #bush
                elif cell_value == 7: self.type = 6     #river 
                self.cord = (y, x)
                self.g = 10**9
                self.h = abs(x - fx) + abs(y - fy)
                self.f = 10**9
                self.nearby = (
                              (y+1, x),
                              (y-1, x),
                              (y, x+1),
                              (y, x-1),)
                self.parent = None
        
                
        def __hash__(self):
            return hash(self.cord)

        def __eq__(self, other):
            return self.cord == other.cord        
              
      
      def pathfinder(self, entrance, finish):
        entrance = tuple(entrance)
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
            if current == start:
                self.grid[current.cord[0]][current.cord[1]] = 11
            else:
                self.grid[current.cord[0]][current.cord[1]] = 1
            if current.cord == tuple(finish):
                update_grid(self.grid,current.cord) 
                return retrace(self.grid,current,finish)

            for n in current.nearby:
                # ignores walls
                if self.grid[n[0]][n[1]] not in (0,5,6,7):
                    continue

                neighbour = get_node(n)

                if neighbour in closed_set: #if the neighbour has been already visited skip this step
                    continue

                tentative_g = current.g + neighbour.type

                if tentative_g < neighbour.g:
                    neighbour.g = tentative_g
                    neighbour.f = tentative_g + neighbour.h
                    neighbour.parent = current
                    counter += 1

                    
                    if neighbour not in open_set: # if the neighbour has not been searched yet add it to the candidates
                        heapq.heappush(open_list, (neighbour.f, neighbour.h, counter, neighbour))
                        open_set.add(neighbour)
            
            def retrace(grid, current,finish):
                last = None
                while current is not None:
                    last = current
                    grid[current.cord[0]][current.cord[1]] = 3
                    current = current.parent
                grid[finish[0]][finish[1]] = 5
                grid[entrance[0]][entrance[1]] = 11
                return update_grid(grid,last.cord)
        return "Couldn't find a path that leads to the exit"