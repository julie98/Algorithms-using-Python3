def quick_sort(list):
	if len(list) < 2:
		return list
	else:
		pivot = list[0]
		less = [i for i in list[1:] if i <= pivot]
		greater = [i for i in list[1:] if i > pivot]
		return quick_sort(less) + [pivot] + quick_sort(greater)

list = [3, 7, 1, 9, 5, 2, 8]
sorted_list = quick_sort(list)
print(sorted_list)