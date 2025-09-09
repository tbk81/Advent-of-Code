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

|---------------------------------------- Part 2 ----------------------------------------|
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

"""
# Part 1
# # Get data into a list
# santa_li = []
# with open("data.txt") as f:
#     data = f.readlines()
#     for l in data:
#         line = l.strip('\n')
#         santa_li.append(line)
#
# print(f"OG list: {len(santa_li)}")
# naughty_strings = ["ab", "cd", "pq", "xy"]
# for line in santa_li:
#     for s in naughty_strings:
#         if s in line:
#             santa_li.remove(line)
#             break
#
# dub_santa_li = []
# santa_nice_li = []
#
#
# # double letter
# def double_char(li):
#     current_char = ""
#     for line in li:
#         for char in line:
#             if char == current_char:
#                 dub_santa_li.append(line)
#                 break
#             current_char = char
#
#
# # Find at least 3 vowels
# # def find_vowels(li):
# #     vowels = ["a", "e", "i", "o", "u"]
# #     for line in li:
# #         vowel_count = 0
# #         for v in vowels:
# #             if v in line:
# #                 vowel_count += 1
# #         if vowel_count >= 3:
# #             santa_nice_li.append(line)
#
#
# def find_vowels(li):
#     vowels = ["a", "e", "i", "o", "u"]
#     for line in li:
#         vowel_count = 0
#         for v in vowels:
#             current_count = line.count(v)
#             vowel_count += current_count
#         if vowel_count >= 3:
#             print(line)
#             print(vowel_count)
#             santa_nice_li.append(line)
#
#
# double_char(santa_li)
# find_vowels(dub_santa_li)
# print(santa_li)
# print(dub_santa_li)
# print(santa_nice_li)
# print(f"Removed naughty string list: {len(santa_li)}")
# print(f"Double list: {len(dub_santa_li)}")
# print(f"Final nice list: {len(santa_nice_li)}")
#
# # for i in dub_santa_li:
# #     print(i)
# # print("\n\n")
# # for i in santa_nice_li:
# #     print(i)
#
# for i in range(len(santa_nice_li)):
#     print(f"{dub_santa_li[i]}\t{santa_nice_li[i]}")

# 205 is too low
# 255 is too high

# import re
#
# with open('data.txt', 'r') as h:
#     datalines = h.readlines()
#
# count = sum(1 for s in datalines
#       if len([x for x in s if x in "aeiou"]) > 2
#       and not any(x in s for x in ["ab", "cd", "pq", "xy"])
#       and re.search(r"([a-z])\1", s)
#  )
# print(count)
#
# count = sum(
#       1 for s in datalines
#       if len(re.findall(r"([a-z]{2}).*\1", s))
#       and re.findall(r"([a-z]).\1", s)
#  )
# print(count)

# Part 2
