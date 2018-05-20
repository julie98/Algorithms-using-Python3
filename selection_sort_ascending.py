def find_smallest(arr):
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[smallest_index] > arr[i]:
			smallest_index = i
	return smallest_index

def selection_sort(arr):

	new_arr = []
	for i in range(len(arr)):
		smallest_index = find_smallest(arr)
		new_arr.append(arr.pop(smallest_index))
	return new_arr

print("The original order:")
arr = [4, 3, 8, 1, 6, 3, 5, 2, 9]
print(arr)
print("By ascending order:")
new_arr = selection_sort(arr)
print(new_arr)