class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0: return False
        while n % 2 ==0:
            n //= 2
        return n==1
 
    def isPowerOfTwo2(self, n: int) -> bool:
        if n==0 or n <0: return False
        count = 0
        while n !=0:
            if n & 0x1 == 1: count += 1
            n >>=1
        return count == 1

    def isPowerOfTwo3(self, n: int) -> bool:
        if n<=0: return False
        return n&(n-1) == 0

    def isPowerOfTwo4(self, n: int) -> bool:
        if n<=0: return False
        return n&(-n) == n
