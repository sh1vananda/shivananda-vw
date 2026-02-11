def alternating(nums):
    for num in range(0, len(nums), 2):
        print(nums[num], end=" ")

nums = list(map(int, input("enter numbers: ").split()))
alternating(nums)