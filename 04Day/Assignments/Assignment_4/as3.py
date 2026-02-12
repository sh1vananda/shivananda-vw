def unique(l1, l2):
    s2 = set(l2)
    res = [] # set instead to avoid duplicates
    for num in l1:
        if num not in l2:
            res.append(num)
    return res

print(unique([10, 20, 30, 40], [30, 40, 50, 60]))