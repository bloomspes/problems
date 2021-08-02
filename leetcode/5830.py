'''
Given an integer n, return true if n has exactly three positive divisors. 
Otherwise, return false.
An integer m is a divisor of n if there exists an integer k such that n = k * m.
'''

class Solution:
    def isThree(self, n: int) -> bool:
        count = len([i for i in range(1, n+1) if n % i == 0])
        return count == 3

