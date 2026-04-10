# ------------------------------------------------ DATA PARSING ----------------------------------------------- #
with open("test_data.txt") as f:
    data = f.readlines()
    data_li = [line.split(",") for line in data]
# print(data_li)

inner_list = data_li[0]
parse_li = [[int(x) for x in s.split('-')] for s in inner_list]
# print(parse_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #
for i in range(len(parse_li)):
    for n in range(parse_li[i][0], parse_li[i][1]+1):
        for digit in str(n):

            print(int(digit))
        print("\n")
    print("\n")


