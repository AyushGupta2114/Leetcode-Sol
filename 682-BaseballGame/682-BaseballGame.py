                score.append(score[-1]*2)
            elif(i=="+"):
                score.append(int(score[-1])+int(score[-2]))
            else:
                score.append(int(i))
            print(score)
        return sum(score)


        
[
