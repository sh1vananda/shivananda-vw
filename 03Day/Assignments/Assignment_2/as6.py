def largest_number(nums):
    curr_max = float('-inf')
    for num in nums:
        if num > curr_max:
            curr_max = num
    return curr_max

nums = list(map(int, input("enter nums: ").split()))
print(largest_number(nums))