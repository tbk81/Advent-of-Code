with open("test_data.txt") as f:
    data = f.readlines()
    data_li = [line.strip() for line in data]
print(data_li)

# -------------------------------------------------- PART 1 -------------------------------------------------- #

for num in data_li:
    for n in num:
        print(n)
    print("\n")
