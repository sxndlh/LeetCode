class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 队列（滑动窗口）
        sublen = []
        suml = 0
        i = 0
        if len(nums)==0:
            return 0
        for j in range(0,len(nums)):
            suml += nums[j]
            if suml >= s:
                sublen.append(j-i+1)
                while (suml-nums[i] >= s):
                    suml = suml-nums[i]
                    i += 1
                sublen.append(j-i+1)
            elif j == len(nums)-1:
                sublen.append(int(suml>=s))
        return min(sublen)