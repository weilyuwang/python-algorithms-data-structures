'''
Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. The function should find all quadruplets in
the array that sum up to the target sum and return a two-dimensional array of
all these quadruplets in no particular order.

If no four numbers sum up to the target sum, the function should return an
empty array.

Sample input:
array = [7, 6, 4, -1, 1, 2]
targetSum = 16

Sample Output:
[[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently
'''


def fourNumberSum(array, targetSum):
	results = []
	allPairSums = {}
	
	for i in range(1, len(array) - 1):
		for j in range(i + 1, len(array)):
			curSum = array[i] + array[j]
			diff = targetSum - curSum
			if diff in allPairSums:
				for pair in allPairSums[diff]:
					results.append(pair + [array[i], array[j]])
			
		for k in range(0, i):
			curSum = array[i] + array[k]
			if curSum not in allPairSums:
				allPairSums[curSum] = [[array[k], array[i]]]
			else:
				allPairSums[curSum].append([array[k], array[i]])

	return results;

                
input_array = [7, 6, 4, -1, 1, 2]
target_sum = 16
print(fourNumberSum(input_array, target_sum))