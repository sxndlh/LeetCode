class Solution:
    def numWays(self, n: int) -> int:
        a = 1
        b = 1
        for i in range(n-1):
            a, b = b, a+b
        return b%1000000007