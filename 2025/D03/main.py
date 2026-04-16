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

num = '811111111111119'
first_num = 0
first_pos = 0
second_num = 0
second_pos = 0
num_li = list(map(int, num))  # creates a list of int from a str
print(num_li)
for i in range(len(num_li)):
    if num_li[i] > first_num:
        first_num = num_li[i]
        first_pos = i
    # print(i)
print(first_num, first_pos)

# for n in num:
#     if int(n) > first_num:
#         first_num = int(n)
