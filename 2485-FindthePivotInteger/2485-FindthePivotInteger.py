        #     i+=1
        #     if(a==b):
        #         x=False
        # print(i)
        #     print(a,b)

        for i in range(1,n+1):
            a=int((i*(i+1))/2)
            b=int(((n-i+1)/2)*(n+i))
            if a==b:
                return i
            print(a,b)
        #     b+=i
        return -1
            

8
