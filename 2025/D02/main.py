import re

# ------------------------------------------------ DATA PARSING ----------------------------------------------- #
with open("test_data.txt") as f:
    data = f.readlines()
    data_li = [line.split(",") for line in data]
# print(data_li)

inner_list = data_li[0]
parse_li = [[int(x) for x in s.split('-')] for s in inner_list]
# print(parse_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #
def find_pattern(full_number, min_length=1):
    """
    Scans a number to find ANY sequence of digits (of min_length or more)
    that repeats.
    """
    str_num = str(full_number)

    # Regex Explanation:
    # (\d{min_length,}) -> Capture a group of digits of size min_length or larger
    # .*?               -> Match any characters in between (non-greedy)
    # \1                -> Match the EXACT same group captured in step 1
    pattern = fr"(\d{{{min_length},}}).*?\1"

    match = re.search(pattern, str_num)

    if match:
        found_pattern = match.group(1)
        return True, found_pattern
    return False, None


for i in range(len(parse_li)):
    for n in range(parse_li[i][0], parse_li[i][1] + 1):
        print(n)
        pattern = find_pattern(n)
        print(pattern)
        # print("\n")
    print("\n")

# --- Testing the code ---
# my_num = 98555025550
# has_repeats, pattern = find_pattern(my_num, min_length=3)
#
# if has_repeats:
#     print(f"Found a repeating pattern: '{pattern}'")
# else:
#     print("No repeating patterns found.")


# -------------------------------------------------- TESTING -------------------------------------------------- #
# for i in range(len(parse_li)):
#     for n in range(parse_li[i][0], parse_li[i][1]+1):
#         for digit in str(n):
#             print(int(digit))
#         print("\n")
#     print("\n")

# regex = re.compile(r'(.+ .+)( \1)+')
# match = regex.search('3 0 5 5 1 5 1 6 8')
# match.group(0)    # entire match
# '5 1 5 1'
# match.group(1)    # repeating portion
# '5 1'
# match.start()     # start index of repeating portion
# 6
# match = regex.search('2 0 6 3 1 6 3 1 6 3 1')
# match.group(1)
# '6 3 1'
