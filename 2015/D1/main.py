"""
|---------------------------------------- Part 1 ----------------------------------------|
Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he
 got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at
  a time.
An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
For example:
    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

|---------------------------------------- Part 2 ----------------------------------------|
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?

"""

# Part 1
# with open("data.txt") as f:
#     data = f.readlines()
#     up_count = 0
#     down_count = 0
#     for line in data:
#         up_count += line.count("(")
#         down_count -= line.count(")")
#     total = up_count + down_count
#     print(total)


# Part 2
with open("data2.txt") as f:
    data = f.readlines()
    total = 0
    for i in range(len(data[0])):
        if data[0][i] == "(":
            total += 1
        elif data[0][i] == ")":
            total -= 1

        if total == -1:
            print(i)


