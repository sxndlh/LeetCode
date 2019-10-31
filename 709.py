# ord():返回str对应的 ASCII 数值，或者 Unicode 数值
# join():将序列中的元素以指定的字符连接生成一个新的字符串
'''
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print str.join( seq );
'''
# 输出：a-b-c

class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(c)+32) if ord(c)>=65 and ord(c)<=90 else c for c in str])
# str.lower()函数
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()