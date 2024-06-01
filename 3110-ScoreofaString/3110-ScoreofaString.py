class Solution:
    def scoreOfString(self, s: str) -> int:
        a=0
        for i in range(0,len(s)-1):
            a+=abs(ord(s[i+1])-ord(s[i]))
        print(a)
        return a
            # print(ord(s[i]))
        
"
