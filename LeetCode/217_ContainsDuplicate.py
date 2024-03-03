nums = [1, 2, 3, 1]


def isDuplicate(arr):
    dict1 = {}
    for i in range(len(arr)):
        if arr[i] in dict1:
            return True
        dict1[arr[i]] = True
    return False


isDublicate_arr = isDuplicate(nums)
print(isDublicate_arr)
