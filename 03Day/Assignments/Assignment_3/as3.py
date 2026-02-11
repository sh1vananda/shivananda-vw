# 3) Write a Python program to count the elements in a list until an element is a
# tuple.
# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3

def count(lst):
    c = 0
    for ele in lst:
        if type(ele) == tuple:
            break
        c += 1
    return c

lst = [10, 20, 30, 40, 50, 60]

c = count(lst)

if c == len(lst):
    print(f"count: {count(lst)}, no tuple found")
else:
    print(f"count: {count(lst)}")