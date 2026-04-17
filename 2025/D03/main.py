import heapq
from itertools import combinations

with open("data.txt") as f:
    data = f.readlines()
    data_li = [line.strip() for line in data]
# print(data_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #

# def joltage(num):
#     num_li = list(map(int, num))
#     top = heapq.nlargest(2, num_li)
#     pos1 = num_li.index(top[0])
#     pos2 = num_li.index(top[1])
#     if pos1 < pos2:
#         fin_num = int(str(top[0]) + str(top[1]))
#     else:
#         fin_num = int(str(top[1]) + str(top[0]))
#     return fin_num


# joltage_li = []
# for i in data_li:
#     joltage_li.append(joltage(i))
# print(joltage_li)
# print(joltage(test_num))

# def find_joltage(num):
#     num_li = list(map(int, num))
#     all_combos = [int(f"{a}{b}") for a, b in combinations(num_li, 2)]
#     return max(all_combos)
#
#
# joltage_li = []
# for i in data_li:
#     joltage_li.append(find_joltage(i))
# print(joltage_li)
# print(sum(joltage_li))

# -------------------------------------------------- PART 2 -------------------------------------------------- #

def find_joltage(num):
    num_li = list(map(int, num))
    all_combos = [int("".join(map(str, combo))) for combo in combinations(num_li, 12)]
    return max(all_combos)


joltage_li = []
for i in data_li:
    joltage_li.append(find_joltage(i))
# print(joltage_li)
print(sum(joltage_li))

