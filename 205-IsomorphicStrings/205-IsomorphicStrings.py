class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # x=Counter(s)
        # y=Counter(t)
        # if(list(x.values())!=list(y.values())):
        #     # print(list(x.values()),list(y.values()))
        #     return False
        a={}
        for i in range(0,len(s)):
            if(t[i] in a):
                if(a[t[i]]!=s[i]):
                    return False   
            else:
                if(s[i] in list(a.values())):
                    return False
                a[t[i]]=s[i]
                # print(a)
"egg"
