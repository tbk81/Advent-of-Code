import numpy as np


# def txt_arr_parse(txt):
#     with open(txt) as f:
#         return [l.strip().split(' ') for l in f.readlines()]


# data_li = txt_arr_parse("test_data.txt")
# data_arr = np.array(data_li)

# arr = np.loadtxt("test_data.txt", dtype=str, delimiter=" ")
# print(arr)
# print(arr.shape)
# -------------------------------------------------- PART 1 -------------------------------------------------- #

def count_accessible_rolls(grid_text):
    # Convert the raw text into a 2D grid (list of strings)
    grid = [line.strip() for line in grid_text.strip().split('\n')]
    rows = len(grid)
    cols = len(grid[0])

    accessible_count = 0

    # Define the 8 adjacent directions as (row_offset, col_offset)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
        (0, -1), (0, 1),  # Left, Right
        (1, -1), (1, 0), (1, 1)  # Bottom-left, Bottom, Bottom-right
        ]

    # Iterate through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Cells that have a roll of paper
            if grid[r][c] == '@':
                adjacent_rolls = 0

                # Check all 8 neighboring positions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Ensure the neighbor is within the grid boundaries
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            adjacent_rolls += 1

                # If fewer than 4 adjacent rolls, the forklift can access it
                if adjacent_rolls < 4:
                    accessible_count += 1

    return accessible_count



result = count_accessible_rolls('data.txt')
print(f"Accessible paper rolls in example: {result}")





# -------------------------------------------------- PART 2 -------------------------------------------------- #



# -------------------------------------------------- TESTING ---------------------------------------------- #

# def txt_parse(txt):
#     with open(txt) as f:
#         data = f.readlines()
#         return [l.strip() for l in data]

# with open("test_data.txt") as f:
#     data_arr = [l.strip().split(' ') for l in f.readlines()]

# for x in np.nditer(data_arr, flags=['external_loop']):
#     print(x, end=' ')
# print("\n")
# for x in np.nditer(data_arr, flags=['external_loop'], order='F'):
#     print(x, end=' ')

# print(data_arr[0])
# print(data_arr[0][0])
# print(data_arr[0][0][0])
# for li in data_arr:
#     counter = 0
#     for element in li:
#         for i in element:
#             if i == '@':
#                 print('@')
#         print("\n")

# print(data_arr)
# print(data_arr.shape)

# ROWS, COLS = len(arr), len(arr[0])
# ROWS, COLS = len(grid), len(grid[0])
# some more code ...

# top, top right, right, bottom right, bottom, bottom left, left, top left
# directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# while queue:
#     row, col = queue.popleft()
#     for d in directions:
#         neighbor_row, neighbor_col = row + d[0], col + d[1]
#         if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
#             pass
            # do something, e.g. BFS ...

# https://andrei.poehlmann.dev/post/visiting-all-neighs-in-grid/






