import time
import os
import sys
import keyboard
import tracemalloc
import generator
import astar    
sys.setrecursionlimit(1500)



previous = []
entrance = [2,2]
finish = [20,90]
tracemalloc.start()
start = time.perf_counter()
current_grid = generator.random_grid(entrance,previous,finish)
end = time.perf_counter()
print("maze generation time:", end - start)
time.sleep(5)
entrance = (2,2)
current_step = entrance
previous = []
columns = len(current_grid[0])
start = time.perf_counter()
a = astar.aStar(entrance,current_grid,finish)
a.pathfinder(entrance,finish)
current, peak = tracemalloc.get_traced_memory()
end = time.perf_counter()
print("maze solve time:", end - start)
print(f"Current memory usage: {current / 1024:.2f} KB")
print(f"Peak memory usage: {peak / 1024:.2f} KB")
tracemalloc.stop()
time.sleep(10)



