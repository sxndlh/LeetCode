1.短路运算符就是从左到右的运算中前者满足要求，就不再执行后者了
class Solution:
    def sumNums(self, n: int) -> int:
        return n != 0 and n + self.sumNums(n - 1)

2.
class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(1, n+1))
