g_score ={cell: float ('inf') for cell in all_cells}
      f_score = {cell: float('inf') for cell in all_cells}
      g_score[entrance]=0
      f_score[entrance]=h(entrance,(2,2))
      

      open = []
      heapq.heapify(open)
      heapq.heappush(open, (h(entrance, (2,2)), h(entrance, (2,2)), entrance))
      aPath ={}
      while open:
        currCell=open[0][2]
        currCell = list(currCell)
        nearby_cell = [current_grid [currCell[0] + 1][currCell[1]],current_grid [currCell[0] - 1][currCell[1]],current_grid [currCell[0]][currCell[1]+1],current_grid [currCell[0]][currCell[1]-1]]
        if currCell==(2,2):
            break
    

        if nearby_cell[2] not in [1,2,3]:
                    childCell=(currCell[0],currCell[1]+1)
        if nearby_cell[1] not in [1,2,3]:
                    childCell=(currCell[0],currCell[1]-1)
        if nearby_cell[3] not in [1,2,3]:
                    childCell=(currCell[0]-1,currCell[1])
        if nearby_cell[0] not in [1,2,3]:
                    childCell=(currCell[0]+1,currCell[1])
        
        temp_g_score=g_score[currCell]+1
        temp_f_score=temp_g_score+h(childCell,(1,1))
        if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    heapq.heappush(open, (temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell] = currCell