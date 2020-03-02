1.自己码的
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        length = len(nums)-1
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                for j in range(length,-1,-1):
                    if i>j:
                        return nums
                    if nums[j]%2 == 1:
                        nums[i], nums[j] = nums[j], nums[i]
                        length = j
                        break
        return nums
2.双指针
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums
3.一行
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        return sorted(nums,key=lambda x:1-x&1)