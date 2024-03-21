        for i in range(0,len(s)):
            if(s[i] in a):
                value=a.get(t[i])
        a={}
        #     return False
        #     # print(list(x.values()),list(y.values()))
        # if(list(x.values())!=list(y.values())):
                if (a[s[i]]!=t[i]):
                    return False
                    
            else:
                a[s[i]]=t[i]
        print(a)
        return True

"
