# address[i] = '[.]'  string（区别于list）是一种不可变的数据类型
class Solution:
    def defangIPaddr(self, address: str) -> str:
        i = 0
        while i < len(address):
            if address[i] == '.':
                address = address[: i] + '[.]' + address[i+1 :]
                i += 3
            else :
                i += 1
        return address