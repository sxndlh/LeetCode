# 先将十进制转化成二进制用list逆序存储
# 将俩个列表补齐再进行比较
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        A = []
        B = []
        while x != 0:
            A.append(x % 2)
            x = x // 2
        while y != 0:
            B.append(y % 2)
            y = y // 2
        #A, B = zip(*zip(A,B))
        if len(A) > len(B):
            for i in range(len(A)-len(B)):
                B.append(0)
        else:
            for i in range(len(B)-len(A)):
                A.append(0)
        cout = 0
        for i in range(max(len(A),len(B))):
            if A[i] != B[i]:
                cout += 1
        return cout
