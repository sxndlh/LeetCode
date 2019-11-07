class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 队列（滑动窗口）
        l = list(s)
        sublen = []
        i = 0
        for j in range(1,len(l)):
            if l[j] in l[i:j]:
                sublen.append(j-i)
                while l[i] != l[j]:
                    i += 1
                i += 1
            elif j == len(l)-1:
                sublen.append(j-i+1)
        if len(l) == 0:
            return 0
        if len(l) == 1:
            return 1
        else:
            return max(sublen)