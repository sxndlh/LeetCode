class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        key = 1
        if len(nums) < 3:
            return True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                
                if i == 0:
                    nums[i] = nums[i+1]
                    key = 0
                elif i == len(nums)-2 and key == 1:
                        return True
                elif i == len(nums)-2 and key != 1:
                        return False  
                elif (nums[i-1]<=nums[i]<=nums[i+2] or nums[i-1]<=nums[i+1]<=nums[i+2]) and key==1:
                    key = 0
                else:
                    return False
        return True
