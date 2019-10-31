# str.count():返回子字符串在字符串中出现的次数
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        i = 0
        for j in range(len(s)):
            if s[i:j].count("R") == s[i:j].count("L"):
                count += 1
                i = j
        return count

# 循环遍历字符串，用字典统计其次数，比较L和R是累加的过程
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        sum = 0
        dict = {'L':0,'R':0}
        for i in s:
            dict[i] += 1
            if dict['L'] == dict['R']:
                sum += 1
        return sum