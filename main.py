import time
import os
import sys
import tracemalloc
import generator
import astar
import editor
sys.setrecursionlimit(1500)


def safe_input_number(prompt="> "):
    while True:
        val = input(prompt).strip()
        if not val.isdigit():
            continue
        return int(val)

current_grid = 0
visuals = False
while True:
    print("Insert 1 to generate a random grid\n")
    print("Insert 2 to create an empty grid and edit it\n")
    print("Insert 3 to exit")
    user_input = safe_input_number("> ")

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
        print("\nDo you want to edit the maze to add other obstacles?y/n")
        choice = input("\n>")
        if choice.lower() == "y" or choice.lower() == "yes":
            entrance,finish,current_grid = editor.editor(entrance,current_grid,finish)
            choice = 0

        else:
            print("ok")
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

    if user_input == 2:
        previous = []
        entrance = [2,2]
        finish = [2,3]
        current_grid = editor.create_grid(entrance,previous,finish)
        entrance,finish,current_grid = editor.editor(entrance,current_grid,finish)
        #time.sleep(3)
        entrance = tuple(entrance)
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

    if user_input == 3:
        exit()
    else:
        print("Invalid input")
    user_input = 0
