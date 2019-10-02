# Algorithm for Kadane's max sum contigious subarray

def maxsum_subarray(arr):
	curr = arr[0]
	maxx = arr[0]
	n = len(arr)

	for i in range(1,n):
		curr = max(arr[i],curr+arr[i])
		maxx = max(curr,maxx)

	return maxx


