# import heapq
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

def get_max_joltage(bank_string, k=12):
    """
    Finds the largest k-digit number from a string of digits
    while preserving the original left-to-right order.
    """
    stack = []

    # This is how many digits allowed to "throw away"
    drop_count = len(bank_string) - k

    for digit in bank_string:
        # If the current digit is BIGGER than the last digit saved and  still allowed to throw numbers away,
        # throw the smaller number away
        while drop_count > 0 and stack and stack[-1] < digit:
            stack.pop()
            drop_count -= 1

        stack.append(digit)

    # Reached the end but still need to throw numbers away
    # (e.g., the numbers were already descending like 9876),
    # chop them off the end.
    while drop_count > 0:
        stack.pop()
        drop_count -= 1

    return int("".join(stack))


total_output_joltage = 0
for bank in data_li:
    max_joltage = get_max_joltage(bank, 12)
    print(f"Bank max: {max_joltage}")
    total_output_joltage += max_joltage

print(f"\nPart Two Answer: {total_output_joltage}")

