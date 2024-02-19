class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1: return False
        ans = log(n, 2)
        return abs(ans - round(ans)) < 1e-10
        
1
