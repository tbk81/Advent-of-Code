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

"""
import numpy as np

instructions = []
parse_li = []
with open("test_data.txt") as f:
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
#
# light_li = []
# for i in range(len(parse_li)):
#     height = abs(parse_li[i][1][0] - parse_li[i][2][0]) + 1
#     width = abs(parse_li[i][1][1] - parse_li[i][2][1]) + 1
#     total = height * width
#     light_li.append([parse_li[i][0], total])
#
print(parse_li)
# print(light_li)

arr = np.zeros((1000, 1000), int)
print(arr)
arr[0, 0] = 100
print(arr)

