def unique(strs):
    seen = set()
    res = []
    for s in strs:
        if s not in seen:
            res.append(s)
            seen.add(s)
    return res

print(unique(input("enter a string: ")))