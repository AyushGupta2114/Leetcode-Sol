        #     if(a==b):
        #         x=False
        # print(i)

        for i in range(1,n+1):
            a=int((i*(i+1))/2)
            b=int(((n-i+1)/2)*(n+i))
            print(a,b)
            if a==b:
                return i
        return -1
        #     print(a,b)
        #     b+=i
        #     i+=1
        #     n-=1
        #     a+=n
        # while(x):
        # x=True
8
