1.
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

2.n & (n - 1) 可以消除 n 最后的一个1
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count