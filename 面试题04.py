1.暴力求解
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # n = matrix.shape[0]
        # m = matrix.shape[1]
        # n,m = matrix.shape
        # matrix是一个二维数组，要先判断行数，再判断列数
        n = len(matrix)
        if n==0:
            return False
        m = len(matrix[0])
        if m==0:
            return False 
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
        return False

2.左下角标志数法
标志数引入： 此类矩阵中左下角和右上角元素有特殊性，称为标志数。
左下角元素： 为所在列最大元素，所在行最小元素。
右上角元素： 为所在行最大元素，所在列最小元素。

标志数性质： 将 matrix 中的左下角元素（标志数）记作 flag ，则有:
若 flag > target ，则 target 一定在 flag 所在行的上方，即 flag 所在行可被消去。
若 flag < target ，则 target 一定在 flag 所在列的右方，即 flag 所在列可被消去。

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    i,j = len(matrix)-1,0
    while i>=0 and j<len(matrix[0]):
        if matrix[i][j] > target:
            i = i - 1
        elif matrix[i][j] < target:
            j = j + 1
        else:
            return True
    return False 

