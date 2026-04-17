import heapq

with open("test_data.txt") as f:
    data = f.readlines()
    data_li = [line.strip() for line in data]
print(data_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #

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


# joltage_li = []
# for i in data_li:
#     joltage_li.append(joltage(i))
# print(joltage_li)
# print(joltage(test_num))

test_num = '818181911112111'
num_li = list(map(int, test_num))
num = 0
for i in range(len(num_li)):
    run_num = int(str(num_li[i]) + str(num_li[i+1]))
    print(run_num)