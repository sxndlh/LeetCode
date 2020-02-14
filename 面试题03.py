class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0) + 1
            # dict.get return key(num)对应的value(default is 0)
            if dic[num] > 1:
                return num