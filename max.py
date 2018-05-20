def find_max(list):
	max = list[0]
	for i in range(1, len(list) ):
		if list[i] > list[0]:
			max = list[i]
	return max

list = [1, 2, 3, 4, 5]
max = find_max(list)
print(max)
 