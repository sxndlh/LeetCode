# 满足的情况：
# 1.两个字符串相同and字符串中有重复元素存在
# 2.两个字符串长度相等andA只有两人位置字符与B不同且交换后与B相同
# set是个查重复元素的好工具（借鉴）
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        # 情况一
        elif A == B and len(A) > len(set(A)):
            return True
        # 情况二，以列表的形式取出A，B中不同的元素
        res = [(a, b) for a, b in zip(A, B) if a != b]
        # 利用切片操作res[1][:,:,-1]将列表翻转
        if len(res) == 2 and res[0] == res[1][::-1]:
            return True
        else:
            return False
