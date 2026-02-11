def histogram(nums):
    for num in nums:
        print("*"*num)

nums = list(map(int, input("enter lengths: ").split()))

histogram(nums)