def list_len(list):
	if list == []:
		return 0
	else:
		return 1 + list_len(list[1:])

list = [1, 2, 3, 4, 5]
length = list_len(list)
print(length)