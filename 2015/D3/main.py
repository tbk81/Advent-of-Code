"""
|---------------------------------------- Part 1 ----------------------------------------|
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him
via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the North Pole has had a little too much eggnog, and so his directions are a little off, and
Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

|---------------------------------------- Part 2 ----------------------------------------|
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents
with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns
moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""
# Part 1
# from collections import Counter
#
# with open("data.txt") as f:
#     line = f.readlines()
# print(line)
# coord_li = [(0, 0)]
# current_coord = [0, 0]
# for i in range(len(line[0])):
#     if line[0][i] == ">":
#         current_coord[0] += 1
#         coord_li.append((current_coord[0], current_coord[1]))
#     elif line[0][i] == "<":
#         current_coord[0] -= 1
#         coord_li.append((current_coord[0], current_coord[1]))
#     elif line[0][i] == "^":
#         current_coord[1] += 1
#         coord_li.append((current_coord[0], current_coord[1]))
#     elif line[0][i] == "v":
#         current_coord[1] -= 1
#         coord_li.append((current_coord[0], current_coord[1]))
#
# # print(coord_li)
# counts = Counter(coord_li)  # This was the answer

# Part 2
from collections import Counter

with open("data.txt") as f:
    line = f.readlines()
# print(line)
santa_li = []
robo_li = []
for i in range(len(line[0])):
    if i%2 == 0:
        santa_li.append(line[0][i])
    elif i%2 == 1:
        robo_li.append(line[0][i])
# print(santa_li)
# print(robo_li)


def coord_maker(li):
    coord_li = [(0, 0)]
    current_coord = [0, 0]
    for i in range(len(li)):
        if li[i] == ">":
            current_coord[0] += 1
            coord_li.append((current_coord[0], current_coord[1]))
        elif li[i] == "<":
            current_coord[0] -= 1
            coord_li.append((current_coord[0], current_coord[1]))
        elif li[i] == "^":
            current_coord[1] += 1
            coord_li.append((current_coord[0], current_coord[1]))
        elif li[i] == "v":
            current_coord[1] -= 1
            coord_li.append((current_coord[0], current_coord[1]))
    return coord_li

santa = coord_maker(santa_li)
robo = coord_maker(robo_li)
robo_santa = santa + robo
# print(robo_santa)
counts = Counter(robo_santa)  # This was the answer
print(counts)
print(len(counts))
