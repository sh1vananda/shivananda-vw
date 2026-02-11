d = {'key 1': 200, 'key 2': 300}

# res = sum(d.values())

res = 0

for k, v in d.items():
    res += v

print(f"Result: {res}")