def binary_search(arr, target):
	low = 0
	high = len(arr) - 1
	
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid -1
	return None

arr = [2, 3, 6, 8, 11, 15, 17]
print(binary_search(arr, 5))
print(binary_search(arr, 11))

arr = [1, 2, 3, 4, 5, 6]
print(binary_search(arr, 8))
