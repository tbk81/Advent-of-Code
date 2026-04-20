import numpy as np


def txt_arr_parse(txt):
    with open(txt) as f:
        return [l.strip().split(' ') for l in f.readlines()]


data_li = txt_arr_parse("test_data.txt")
data_arr = np.array(data_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #

print(data_arr)
print(data_arr.shape)

# ROWS, COLS = len(grid), len(grid[0])
# some more code ...

# top, top right, right, bottom right, bottom, bottom left, left, top left
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# while queue:
#     row, col = queue.popleft()
#     for d in directions:
#         neighbor_row, neighbor_col = row + d[0], col + d[1]
#         if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
#             pass
            # do something, e.g. BFS ...

# https://andrei.poehlmann.dev/post/visiting-all-neighs-in-grid/





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







