def union(l1, l2):
    seen = set()
    res = []
    for i in l1:
        if i not in seen:
            res.append(i)
            seen.add(i)
    for i in l2:
        if i not in seen:
            res.append(i)
            seen.add(i)
    return res

print(union([10, 20, 30, 40], [30, 40, 50, 60]))