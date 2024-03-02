nums = [2, 7, 9, 11]
target = 9


def twoSums(nums, target):
    dict1 = {}
    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in dict1:
            return [dict1[complement], i]
        dict1[nums[i]] = i


solution = twoSums(nums, target)
print(solution)
