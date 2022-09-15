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

Intuition

Think in terms of bits of product which we will obtain after multiplying the given numbers from the subset.
Implementation

From the properties of power of two, we can see that it can be expressed only as a product of numbers which itself is the power of 2.

Proof : Suppose the numbers are power of 2 in the subset. Then only one bit will be set in each of those numbers . So if we will multiply them, then also there will be only one bit set in the product of them. 

Example : If the subset is s=[2,4,8] . So we can represent them as [21, 22, 23] . Now if we multiply them then product equals 26. It has only one bit set (i.e. 6th bit) . So it is also power of 2. 

So , we will count the number of elements in the array which are the power of 2 . 
Then our final answer will be 2count-1. We subtracted 1 because we want non empty subsequence.
Also don't forget to modular multiplication since answer can overflow.

Note : Don't use inbuilt power function because we have to use modulo operation . So use fast exponentiation with modulo operation instead of it.
Complexity

Time Complexity: O(N), where N is size of the array.
Space Complexity : O(1), no extra space is used.
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
