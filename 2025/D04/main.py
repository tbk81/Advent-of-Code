import numpy as np


def txt_arr_parse(txt):
    with open(txt) as f:
        return [l.strip().split(' ') for l in f.readlines()]


data_arr = txt_arr_parse("test_data.txt")
print(data_arr)

# -------------------------------------------------- PART 1 -------------------------------------------------- #



# -------------------------------------------------- PART 2 -------------------------------------------------- #



# -------------------------------------------------- TESTING ---------------------------------------------- #

# def txt_parse(txt):
#     with open(txt) as f:
#         data = f.readlines()
#         return [l.strip() for l in data]

# with open("test_data.txt") as f:
#     data_arr = [l.strip().split(' ') for l in f.readlines()]
