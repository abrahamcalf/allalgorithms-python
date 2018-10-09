#
# Linear Search
# Works for a Sorted or Unsorted Array
# Apart of the All Algorithms Library for Python
#
# Contributed by Jason Tomlin
# Github: @JasonJTomlin
#
def linear_search(arr,value):
	rangeEnd = len(arr) - 1
	count = 0
	while (count <= rangeEnd):
		if (value == arr[count]):
			return count
		count = count + 1
	return None
