import re
# ------------------------------------------------ DATA PARSING ----------------------------------------------- #
with open("test_data.txt") as f:
    data = f.readlines()
    data_li = [line.split(",") for line in data]

inner_list = data_li[0]
parse_li = [[int(x) for x in s.split('-')] for s in inner_list]

# -------------------------------------------------- PART 1 -------------------------------------------------- #

def li_maker(li):
    """
    Take a list from the parsed list and inserts the numbers that in range of the 2 numbers i.e., 11 thorough 22
    """
    first_num = li[0]
    last_num = li[1] - 1
    num = first_num
    while num < last_num:
        num += 1
        li.insert(len(li)-1, num)
    return li


test_li = [li_maker(li) for li in parse_li]

# (\d+) : Captures one or more digits and groups them (Group 1)
# \1    : Matches the exact same text captured in Group 1
pattern = r"\b(\d+)\1\b"

for i in test_li:
    matches = [match.group(0) for match in re.finditer(pattern, str(i))]

