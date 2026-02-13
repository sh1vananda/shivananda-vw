# .txt, .csv
# read, write, merge, remove

# f = open("text.txt", "r") # modes - r, w, a, x, b, r+, w+
# data = f.read()
# print(data)
# f.close()

# with open("text.txt", "r") as f:
#     data = f.read(13)
#     print(data)

# with open("text.txt") as f:
#     for line in f:
#         print(line, end="")

# with open("text.txt", "w") as f:
#     f.write("line 6")

with open("text.txt", "a") as f:
    f.write("line 7\n")
    f.write("line 8\n")