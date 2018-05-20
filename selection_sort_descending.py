def find_biggest(arr):
	biggest_index = 0
	for i in range(1, len(arr)):
		if arr[i] > arr[biggest_index]:
			biggest_index = i
	return biggest_index

def selection_sort(arr):
	new_arr = []
	for i in range(len(arr)):
		biggest_index = find_biggest(arr)
		new_arr.append(arr.pop(biggest_index))
	return new_arr 

print("The original order:")
arr = [4, 3, 8, 1, 6, 3, 5, 2, 9]
print(arr)
print("By descending order:")
new_arr = selection_sort(arr)
print(new_arr)
