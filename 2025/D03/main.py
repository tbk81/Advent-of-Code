with open("test_data.txt") as f:
    data = f.readlines()
    data_li = [line.strip() for line in data]
print(data_li)

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
second_num = 0
for n in num:
    if int(n) > first_num:
        first_num = int(n)
print(first_num)
