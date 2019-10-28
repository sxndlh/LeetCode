# 先对边界特殊的头尾进行特殊判断
# 之后对一般的中间部分进行限制
# 判断条件为：将两个比较的数取成相同，两个数有一个满足其前后非递减就行
# 注意控制判断条件间的逻辑关系
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        key = 1   # 标志符，限制只修改一次
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
