"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

|---------------------------------------- Part 1 ----------------------------------------|
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and
    none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different
    rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?
"""

# Get data into a list
santa_li = []
with open("data.txt") as f:
    data = f.readlines()
    for l in data:
        line = l.strip('\n')
        santa_li.append(line)
# print(santa_li)
# print(len(santa_li))
# disallowed substrings and remove from a list
naughty_strings = ["ab", "cd", "pq", "xy"]
for line in santa_li:
    for s in naughty_strings:
        if s in line:
            santa_li.pop()
            # print(line)
            # print("yes")
# print(santa_li)
# print(len(santa_li))

nice_string_li = []


# double letter
def double_char(li):
    current_char = ""
    for line in li:
        for char in line:
            if char == current_char:
                current_char = char
            print(char)
        print("\n")


double_char(santa_li)

# Find at least 3 vowels
#  vowels = ["a", "e", "i", "o", "u"]
# for line in santa_li:
#     vowel_count = 0
#     for v in vowels:
#         if v in line:
#             vowel_count += 1
#     if vowel_count >= 3:
#         print(line)
#         print("yes")


# double letter
# current_char = ""
#     for line in li:
#         for char in line:
#             if char == current_char:
#                 print(line)
#                 print(char)
#                 print(current_char)
#                 print("yes")
#             current_char = char
#             # print(char)
#         print("\n")