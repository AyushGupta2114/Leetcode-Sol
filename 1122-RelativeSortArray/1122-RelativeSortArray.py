        a=[]
        b=[]
        for i in arr2:
            if i not in arr1:
                a.append(i)
                arr1.remove(i)
        print(a)
        for i in arr2:
            while(i in arr1):
                b.append(i)
                arr1.remove(i)
        print(b)
        return b+arr1
        print(arr1)
        arr1.sort()

[
