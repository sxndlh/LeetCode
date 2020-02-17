class Solution:
    def printNumbers(self, n: int) -> List[int]:
        list = []
        for i in range(1,10**n):
            list.append(i)
        return list