        elif current_grid [entrance[0] + 1][entrance[1]] != 2 and current_grid [entrance[0] + 1][entrance[1]] != 1:
            entrance[0] = entrance[0] + 1
            current_grid = update_grid(current_grid,entrance)
        elif current_grid [entrance[0] - 1][entrance[1]] != 2 and current_grid [entrance[0] - 1][entrance[1]] != 1:
            entrance[0] = entrance[0] - 1
            current_grid = update_grid(current_grid,entrance)
        elif current_grid[entrance[0]][entrance[1] - 1] != 2