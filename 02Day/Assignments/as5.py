nums = list(map(int, input("enter three numbers: ").split()))

# print(f"max: {max(nums)})

curr_max = float('-inf')

for num in nums:
    if num > curr_max:
        curr_max = num

print(f"max: {curr_max}")