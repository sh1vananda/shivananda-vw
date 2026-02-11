def repeat(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
    return count

nums = (1, 2, 2, 3, 3, 4, 1, 2, 3, 2, 1, 1, 3, 2,)

target = int(input("enter number: "))

print(repeat(nums, target))