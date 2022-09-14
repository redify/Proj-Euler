'''
You are given an array Arr of size N containing non-negative integers. 
Your task is to choose the minimum number of elements such that their sum should be greater than the sum of the rest of the elements of the array.
 
N = 4 
Arr[] = {2, 17, 7, 3}
Output:
1
Explanation:
If we only select element 17, the sum of the 
rest of the elements will be (2+3+7)=12.
So the answer will be 1
'''
 
 def minSubset(self, A,N):
 	A.sort(reverse=True)

	num_of_elements = 1

	base_sum = sumArray(A)
	
	running_sum = 0
	for element in A:
		running_sum += element

		if running_sum > (base_sum-running_sum):
			return num_of_elements

		num_of_elements += 1

def sumArray(A):
	sum = 0
	for element in A:
		sum += element
	
	return sum
