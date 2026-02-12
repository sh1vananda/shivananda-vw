def overlap(l1, l2):
    s2 = set(l2)
    res = [] # res = set() if ignoring duplicates
    for num in l1:
        if num in s2:
            res.append(num)
    return res

res = overlap([10, 20, 30, 40], [30, 40, 50, 60])

print(res)