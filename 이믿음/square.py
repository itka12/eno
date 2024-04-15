size = 5
for i in range(1, size + 1):
    if i == 1 or i == size:
        print("* " * size)
    else:
        print("* " + " " * (size + 1) + "*")
