                    continue
                if(num_of_5>=1):
                else:
                    return False
            else:
                shopper+=20
                if(num_of_10>=1 and num_of_5>=1):
                    num_of_10-=1
                    num_of_5-=1
                shopper-=5
                shopper += i
                num_of_10 += 1
            elif i == 10:
                shopper += i
                num_of_5 += 1
            if i == 5:
                    num_of_5-=1
[
