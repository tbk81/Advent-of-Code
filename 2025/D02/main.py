# ------------------------------------------------ DATA PARSING ----------------------------------------------- #
with open("test_data_2.txt") as f:
    data = f.readlines()
    data_li = [line.split(",") for line in data]
# print(data_li)

inner_list = data_li[0]
parse_li = [[int(x) for x in s.split('-')] for s in inner_list]
# print(parse_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #
# for i in range(len(parse_li)):
#     for n in range(parse_li[i][0], parse_li[i][1]+1):
#         for digit in str(n):
#
#             print(int(digit))
#         print("\n")
#     print("\n")

for i in parse_li:
    first_num = i[0]
    last_num = i[1] - 1
    num = first_num
    num_li = []
    while num < last_num:
        num += 1
        i.insert(len(i)-1, num)
    print(i)


