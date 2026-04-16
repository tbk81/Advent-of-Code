import heapq

with open("test_data.txt") as f:
    data = f.readlines()
    data_li = [line.strip() for line in data]
# print(data_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #

# for num in data_li:
#     for n in num:
#         print(n)
#     print("\n")

# for num in data_li:
#     first_num = 0
#     second_num = 0
#     for n in num:
#         print(n)
    # maximum = max(int(n) for n in num)
    # print(maximum)

test_num = '811111111111119'

def joltage(num):
    num_li = list(map(int, num))
    top = heapq.nlargest(2, num_li)
    pos1 = num_li.index(top[0])
    pos2 = num_li.index(top[1])
    if pos1 < pos2:
        fin_num = int(str(top[0]) + str(top[1]))
    else:
        fin_num = int(str(top[1]) + str(top[0]))
    return fin_num


print(joltage(test_num))
