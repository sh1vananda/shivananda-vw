def overlapping(l1, l2):
    s2 = set(l2)
    for num in l1:
        if num in s2:
            return "overlap: true"
    return "overlap: false"

l1 = [1, 2, 3, 4, 5]
l2 = [3, 6, 7, 8, 9, 10]
print(overlapping(l1, l2))