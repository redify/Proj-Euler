'''
Given is an array A[] of size N. 
Return the number of non-empty subsequences such that the product of all numbers in the subsequence is Power of 2. 
Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input:
N = 3
A[] = {1, 6, 2}
Output:
3
Explanation:
The subsequence that 
can be chosen is {1},
{2} and {1,2}.
'''

def isPowerOfTwo(num):
    if num == 0:
        return False

    return (num & (num-1)) == 0 

def numberOfSubsequences (N,A):
    # power of two = {2^n | n is an integer}
    # positive power of 2 = { 2^n | n is an integer >= 0}
    # 2, 4, 8, 16, 32, 64, 128, 256
    # confirmed powers of two multiplied together will result in an output also a power of two

    counter = 0
    for element in A:
        if isPowerOfTwo(element):
            counter += 1

    return (pow(2, counter) - 1) % 1000000007
