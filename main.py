import time
import os
import sys
import tracemalloc
import generator
import astar
import editor    
sys.setrecursionlimit(1500)

print("Choose 1,2 or 3")
user_input =  int(input(">"))




if user_input == 1:
    previous = []
    entrance = [2,2]
    finish = [20,90]
    tracemalloc.start()
    start = time.perf_counter()
    current_grid = generator.random_grid(entrance,previous,finish)
    end = time.perf_counter()
    print("maze generation time:", end - start)
    time.sleep(3)
    entrance = (2,2)
    previous = []
    start = time.perf_counter()
    a = astar.aStar(entrance,current_grid,finish)
    a.pathfinder(entrance,finish)
    current, peak = tracemalloc.get_traced_memory()
    end = time.perf_counter()
    print("maze solve time:", end - start)
    print(f"Current memory usage: {current / 1024:.2f} KB")
    print(f"Peak memory usage: {peak / 1024:.2f} KB")
    tracemalloc.stop()
    time.sleep(3)

if user_input == 3:
    previous = []
    entrance = [2,2]
    finish = [2,3]
    current_grid = editor.create_grid(entrance,previous,finish)
    entrance,finish,current_grid = editor.editor(entrance,current_grid,finish)
    #time.sleep(3)
    tuple(entrance)
    start = time.perf_counter()
    tracemalloc.start()
    a = astar.aStar(entrance,current_grid,finish)
    a.pathfinder(entrance,finish)
    current, peak = tracemalloc.get_traced_memory()
    end = time.perf_counter()
    print("maze solve time:", end - start)
    print(f"Current memory usage: {current / 1024:.2f} KB")
    print(f"Peak memory usage: {peak / 1024:.2f} KB")
    tracemalloc.stop()
    time.sleep(3)




