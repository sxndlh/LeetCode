# 两个循环遍历
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cout = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i]==S[j]:
                    cout += 1
        return cout
