1.将当前节点的值和指针都修改为下一个节点的值和指针即可，相当于让当前节点冒充下一个节点，那么远离啊的当前节点被修改消除，原来节点的下一位节点因为没有被指针连接而失去意义
此题考查python函数的传参形式为“传对象引用”，相当于浅拷贝（对于可变对象来说）

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next