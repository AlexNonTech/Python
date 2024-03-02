arr1 = []
arr1.append(31)
arr1.append(40)
arr2 = arr1.copy()
arr1.extend(arr2)
arr1.insert(1, 105)

popped_item = arr1.pop()

reversed_arr = arr1.copy()
reversed_arr.reverse()

sorted_arr = arr1.copy()
sorted_arr.sort()

arr1.index(105)
arr1.count(31)


print(reversed_arr)
print(sorted_arr)
print(arr1)
print(arr2)
print(popped_item)