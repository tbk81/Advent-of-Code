import numpy as np


def txt_arr_parse(txt):
    with open(txt) as f:
        return [l.strip().split(' ') for l in f.readlines()]


data_li = txt_arr_parse("test_data.txt")
data_arr = np.array(data_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #

print(data_arr)
# print(data_arr[0])
# print(data_arr[0][0])
# print(data_arr[0][0][0])
# for li in data_arr:
#     for i in li:
#         for j in i:
#             print(j)
#         print("\n")

for i, j in np.argwhere(data_arr == 1):
    print(i, j)







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
