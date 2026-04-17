import numpy as np


# def txt_parse(txt):
#     with open(txt) as f:
#         data = f.readlines()
#         return [l.strip() for l in data]

def txt_arr_parse(txt):
    with open(txt) as f:
        data = f.readlines()
        return [l.strip() for l in data]


data_arr = txt_arr_parse("test_data.txt")
print(data_arr)

