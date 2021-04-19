#Division Pair Sum

def DPS(arr, m):
	rem = {}
	for num in arr:
		if num%m in rem:
			rem[num%m] += 1
		else:
			rem[num%m] = 1
	#print(rem)
	no = 0
	for r in rem:
		pair = 0
		complement = m - r
		if complement == m or 2*complement == m:
			pair = (rem[r]*(rem[r]-1))//2
		elif complement in rem:
			pair = rem[r]*rem[complement]
			rem[r]=0
		no += pair
	return  no
	
print("Enter elements for array :: ", end="")
arr = list(map(int, input().split()))
m = int(input("Enter a number --> "))

print("No. of pairs existing in array whose sum is divisible by {} --> {}".format(m, DPS(arr, m)))



