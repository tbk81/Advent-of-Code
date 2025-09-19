"""
--- Day 6: Probably a Fire Hazard ---

|---------------------------------------- Part 1 ----------------------------------------|
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided
to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the
ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights in each corner are at
0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive
ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive;
a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent
you in order.

For example:

    Turn on 0,0 through 999,999 would turn on (or leave on) every light.
    Toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on and
    turning on the ones that were off.
    Turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

|---------------------------------------- Part 2 ----------------------------------------|
You finish implementing your winning light pattern when you realize you mistranslated Santa's message from
Ancient Nordic Elvish.
The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or
more. The lights all start at zero.
The phrase turn on actually means that you should increase the brightness of those lights by 1.
The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
The phrase toggle actually means that you should increase the brightness of those lights by 2.
What is the total brightness of all lights combined after following Santa's instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""
import numpy as np

instructions = []
parse_li = []
with open("data.txt") as f:
    data = f.readlines()
    for line in data:
        line = line.strip('\n')
        instructions.append(line)
# print(instructions)

for i in instructions:
    line = i.split()
    if line[0] == "toggle":
        line.remove("through")
        parse_li.append(line)
    elif line[0] == "turn":
        line.remove("turn")
        line.remove("through")
        parse_li.append(line)

for i in range(len(parse_li)):
    parse_li[i][1] = list(parse_li[i][1].split(","))
    parse_li[i][2] = list(parse_li[i][2].split(","))

for i in range(len(parse_li)):
    parse_li[i][1][0] = int(parse_li[i][1][0])
    parse_li[i][1][1] = int(parse_li[i][1][1])
    parse_li[i][2][0] = int(parse_li[i][2][0])
    parse_li[i][2][1] = int(parse_li[i][2][1])

light_li = []
for i in range(len(parse_li)):
    height = abs(parse_li[i][1][0] - parse_li[i][2][0]) + 1
    width = abs(parse_li[i][1][1] - parse_li[i][2][1]) + 1
    total = height * width
    light_li.append([parse_li[i][0], total])
#
# print(parse_li)
# print(light_li)

# Part 1
# arr = np.zeros((1000, 1000), int)
# for l in range(len(parse_li)):
#     if parse_li[l][0] == "on":
#         x_range = abs(parse_li[l][1][0] - parse_li[l][2][0]) + 1
#         y_range = abs(parse_li[l][1][1] - parse_li[l][2][1]) + 1
#         for y in range(y_range):
#             for x in range(x_range):
#                 arr[parse_li[l][1][0] + x, parse_li[l][1][1] + y] = 1
#     elif parse_li[l][0] == "off":
#         x_range = abs(parse_li[l][1][0] - parse_li[l][2][0]) + 1
#         y_range = abs(parse_li[l][1][1] - parse_li[l][2][1]) + 1
#         for y in range(y_range):
#             for x in range(x_range):
#                 arr[parse_li[l][1][0] + x, parse_li[l][1][1] + y] = 0
#     elif parse_li[l][0] == "toggle":
#         x_range = abs(parse_li[l][1][0] - parse_li[l][2][0]) + 1
#         y_range = abs(parse_li[l][1][1] - parse_li[l][2][1]) + 1
#         for y in range(y_range):
#             for x in range(x_range):
#                 if arr[parse_li[l][1][0] + x, parse_li[l][1][1] + y] == 0:
#                     arr[parse_li[l][1][0] + x, parse_li[l][1][1] + y] = 1
#                 else:
#                     arr[parse_li[l][1][0] + x, parse_li[l][1][1] + y] = 0
# print(arr)

# Part 2
arr = np.zeros((1000, 1000), int)
for l in range(len(parse_li)):
    if parse_li[l][0] == "on":
        x_range = abs(parse_li[l][1][0] - parse_li[l][2][0]) + 1
        y_range = abs(parse_li[l][1][1] - parse_li[l][2][1]) + 1
        for y in range(y_range):
            for x in range(x_range):
                arr[parse_li[l][1][0] + x, parse_li[l][1][1] + y] += 1
    elif parse_li[l][0] == "off":
        x_range = abs(parse_li[l][1][0] - parse_li[l][2][0]) + 1
        y_range = abs(parse_li[l][1][1] - parse_li[l][2][1]) + 1
        for y in range(y_range):
            for x in range(x_range):
                if arr[parse_li[l][1][0] + x, parse_li[l][1][1] + y] == 0:
                    pass
                else:
                    arr[parse_li[l][1][0] + x, parse_li[l][1][1] + y] -= 1
    elif parse_li[l][0] == "toggle":
        x_range = abs(parse_li[l][1][0] - parse_li[l][2][0]) + 1
        y_range = abs(parse_li[l][1][1] - parse_li[l][2][1]) + 1
        for y in range(y_range):
            for x in range(x_range):
                arr[parse_li[l][1][0] + x, parse_li[l][1][1] + y] += 2

unique, counts = np.unique(arr, return_counts=True)
lit_dict = dict(zip(unique, counts))

brightness = 0
for k in range(1, len(lit_dict)):
    brightness += k * lit_dict[k]
print(brightness)
