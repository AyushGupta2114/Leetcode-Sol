        for i in range(0,len(s)):
            if(t[i] in a):
        a={}
        #     return False
        #     # print(list(x.values()),list(y.values()))
                if(a[t[i]]!=s[i]):
                    return False   
            else:
                a[t[i]]=s[i]
                if(s[i] in list(a.values())):
                    return False
        # x=Counter(s)
        # y=Counter(t)
        # if(list(x.values())!=list(y.values())):
    def isIsomorphic(self, s: str, t: str) -> bool:
class Solution:
"
