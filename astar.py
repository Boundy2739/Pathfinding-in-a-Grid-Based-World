def a_star(entrance,current_step,finish,current_grid,previous):
      rows = len(current_grid)
      cols = len(current_grid[0])
      all_cells = [(r, c) for r in range(rows) for c in range(cols)]
       
      open = []
      closed = []
      heapq.heapify(open)
      heapq.heapify(closed)
      cameFrom = {}
      
      gScore = {cell: ('inf') for cell in all_cells}
      gScore[entrance] = 0
    
      fScore = {cell: ('inf') for cell in all_cells}
      fScore[entrance] = gScore[entrance] + h(entrance,finish)
      heapq.heappush(open,(fScore[entrance],h(entrance,finish),gScore[entrance],entrance))

      while open:
            currF,currH,currG,currCell = heapq.heappop(open)
            update_grid(current_grid,currCell) 
            nearby_cell = [current_grid [currCell[0] + 1][currCell[1]],current_grid [currCell[0] - 1][currCell[1]],current_grid [currCell[0]][currCell[1]+1],current_grid [currCell[0]][currCell[1]-1]]
            if current_grid[finish[0]][finish[1]] == 1:
                  break
            
            heapq.heappush(closed,(currF,currH,currG,currCell))
            if currF != fScore[currCell]:
                continue
            for cell in nearby_cell:
                  if cell not in [1,2,3]:
                        if nearby_cell[0] in [0,5]:
                              neighbour = (currCell[0]+1,currCell[1])
                              newGscore = currG + 1
                              gScore[neighbour] = newGscore
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              fScore[neighbour]=newFscore
                              neighbourset =(newFscore,newHscore,newGscore,neighbour)
                              if neighbourset not in closed:
                                if neighbourset not in open:
                                        heapq.heappush(open,(neighbourset))
                                
                        if nearby_cell[1] in [0,5]:
                              neighbour = (currCell[0]-1,currCell[1])
                              newGscore = currG + 1
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              gScore[neighbour] = newGscore
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              fScore[neighbour]=newFscore
                              neighbourset =(newFscore,newHscore,newGscore,neighbour)
                              if neighbourset not in closed:
                                if neighbourset not in open:
                                        heapq.heappush(open,(neighbourset))
                        if nearby_cell[2] in [0,5]:
                              neighbour = (currCell[0],currCell[1]+1)
                              newGscore = currG + 1
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              gScore[neighbour] = newGscore
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              fScore[neighbour]=newFscore
                              neighbourset =(newFscore,newHscore,newGscore,neighbour)
                              if neighbourset not in closed:
                                if neighbourset not in open:
                                        heapq.heappush(open,(neighbourset))
                        if nearby_cell[3] in [0,5]:
                              neighbour = (currCell[0],currCell[1]-1)
                              newGscore = currG + 1
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              gScore[neighbour] = newGscore
                              newHscore = h(neighbour,finish)
                              newFscore = newGscore + newHscore
                              fScore[neighbour]=newFscore
                              neighbourset =(newFscore,newHscore,newGscore,neighbour)
                              if neighbourset not in closed:
                                if neighbourset not in open:
                                        heapq.heappush(open,(neighbourset))
                

      


      return     
def h(cell1,cell2):
    y1,x1=cell1
    y2,x2=cell2
    return abs(x1-x2) + abs(y1-y2)