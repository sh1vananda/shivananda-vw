def count(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    return d

print(count([1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]))