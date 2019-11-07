class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
	# 字典用散列表来实现存储、查找，也就是哈希表
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
	    # if 写在元素载入之前，避免查找的是同一元素
            hashmap[num] = index
        return None