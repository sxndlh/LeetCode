class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ','%20')
        # 使用replace()函数
class Solution:
    def replaceSpace(self, s: str) -> str:
        s1 = []                       
        for c in s:                  
            if c == ' ':            
                s1.append('%20')        
            else:                       
                s1.append(c)
        return ''.join(s1)