def even_odd(nums):
    d = {"EVEN": [], "ODD": []}
    for num in nums:
        if num % 2 == 0:
            d["EVEN"].append(num)
        else:
            d["ODD"].append(num)
    return d

print(even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))