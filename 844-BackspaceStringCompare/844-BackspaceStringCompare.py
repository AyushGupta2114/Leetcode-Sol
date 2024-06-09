        # print(a)
        for i in t:
            if(i!='#'):
                ab.append(i)
            elif i=='#' and len(ab)!=0:
        ab=[]
                a.pop()
            elif i=='#' and len(a)!=0:
                a.append(i)
                ab.pop()
        print(ab)
        for i in s:
            if i!='#':
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
class Solution:
"
