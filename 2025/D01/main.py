with open("data.txt") as f:
    data = f.readlines()
    data_li = [l.strip() for l in data]
# print(data_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #
current = 50
zero_counter = 0
for c in data_li:
    if c[0] == "L":
        current = (current - int(c[1:])) % 100
        if current == 0:
            zero_counter += 1
        # print(current)
    else:
        current = (current + int(c[1:])) % 100
        if current == 0:
            zero_counter += 1
        # print(current)
print(f'total zeros: {zero_counter}')


# -------------------------------------------------- PART 2 -------------------------------------------------- #
current = 50
zero_counter = 0
for c in data_li:
    if c[0] == "L":
        for i in range(int(c[1:])):
            current = (current - i) % 100
            if current == 0:
                zero_counter += 1
            print(current)
    else:
        for i in range(int(c[1:])):
            current = (current + i) % 100
            if current == 0:
                zero_counter += 1
            print(current)
# print(f'total zeros: {zero_counter}')



# -------------------------------------------------- TESTING -------------------------------------------------- #
# for n in range(200):
#     num = n % 100
#     print(num)

# for n in data_li:
#     print(n[0])

# for n in data_li:
#     print(f"{int(n[1:])} - type: {type(int(n[1:]))}")

# current = 50
# zero_counter = 0
# for c in data_li:
#     if c[0] == "L":
#         for i in range(int(c[1:])):
#             current = (current - i) % 100
#             if current == 0:
#                 zero_counter += 1
#             print(current)
#     else:
#         for i in range(int(c[1:])):
#             current = (current + i) % 100
#             if current == 0:
#                 zero_counter += 1
#             print(current)

