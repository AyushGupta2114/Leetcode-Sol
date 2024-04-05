                return ""
        sama=a
        print(sama)
        if(len(sama)==0):
            return ""
        else:
            for i in range(0,len(s)-1):
                if((s[i]==s[i+1].lower() and s[i].upper()==s[i+1]) or (s[i]==s[i+1].upper() and s[i].lower()==s[i+1])) :
                    del sama[i:i+2]
                print("1")
        if(len(a)==2):
            if(a[0].lower()==a[1]):
        #     return ""
        a=[k for k in s]
class Solution:
    def makeGood(self, s: str) -> str:
        # if(s=="djrDdRJD"):
"leEeetcode"
