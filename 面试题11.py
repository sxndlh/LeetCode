1.
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        return min(numbers)

2.二分法
首先判断数组第一个数是不是小于最后一个数，如果小于，这个数组就是升序的，直接返回第一个数就是最小的。

如果不是那就：每次选取数组中间一个数，如果这个比数组第一个数大，那么他一定在这个数组的前半段，如果他比这个数组最后一个元素小，那他一定在这个数组的后半段。
但是如果相等就无法判断，所以相等的情况同时尝试两种可能。

class Solution:
    def minArray(self, numbers: List[int]) -> int:

        if numbers[0] < numbers[-1]:
            return numbers[0]
        if len(numbers) < 3: 
            return min(numbers)

        mid = len(numbers)>>1  % 等价于 int(len(numbers)/2)
        if numbers[mid] > numbers[0]:
            return self.minArray(numbers[mid+1:])
        if numbers[mid] < numbers[-1]:
            return self.minArray(numbers[:mid+1])
        return min(self.minArray(numbers[mid+1:]), self.minArray(numbers[:mid+1]))

3.遍历
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        if n == 0:
            return 0
        for i in range(1,n):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0]
