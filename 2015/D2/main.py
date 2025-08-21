"""
|---------------------------------------- Part 1 ----------------------------------------|
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the
dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping
paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also
need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of
    slack, for a total of 58 square feet.
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot
    of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

|---------------------------------------- Part 2 ----------------------------------------|
"""
import re

with open("data.txt") as f:
    data = f.readlines()

total = 0
li = [list(map(int, re.findall(r'\d+', num.strip()))) for num in data]
# print(li)
# li = [[4, 23, 21], [22, 29, 19]]
# for i in li:
#     print(i)
for i in li:
    small_num = min([(i[0] * i[1]), (i[1] * i[2]), (i[2] * i[0])])
    two_num = [2*(i[0] * i[1]), 2*(i[1] * i[2]), 2*(i[2] * i[0])]
    sq_ft = sum(two_num) + small_num
    total +=sq_ft
print(total)
