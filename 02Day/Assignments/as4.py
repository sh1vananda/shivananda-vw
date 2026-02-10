def avg(nums):
    return sum(nums) / len(nums)


if __name__ == "__main__":

    nums = list(map(int, input("enter three numbers: ").split()))

    print(f"average: {round(avg(nums))}")