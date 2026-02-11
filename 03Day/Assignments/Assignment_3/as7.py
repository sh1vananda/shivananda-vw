def clean(nums):
    seen = set()
    cleaned_nums = []
    for i in range(0, len(nums) - 1):
        if nums[i] not in seen:
            cleaned_nums.append(nums[i])
            seen.add(nums[i])
    return cleaned_nums

nums = list(map(int, input().split()))

print(clean(nums))