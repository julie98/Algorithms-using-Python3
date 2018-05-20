def sum(arr):
	if(len(arr) == 0):
		return 0
	elif(len(arr) == 1):
		return arr[0]
	else:
		return arr[0] + sum(arr[1:])

arr = [1, 3, 5] 
s = sum(arr)
print(s)