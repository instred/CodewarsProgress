#Given an integer n, return true if it is a power of four. Otherwise, return false.
#An integer n is a power of four, if there exists an integer x such that n == 4x.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n % 4 == 0:
            n = n / 4
        if n == 1:
            return True
        return False
    
#same but with bit checking for n is power of 2 + n%3 == 1 

class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        return n >0 and n & (n-1) == 0 and n%3 == 1


