                if num_of_5 >= 1:
                    num_of_5 -= 1
                    continue
                else:
                    return False
                shopper += 15
                num_of_10 += 1
            elif i == 10:
                shopper += 5
                num_of_5 += 1
        for i in bills:
            if i == 5:
        shopper = 0
        # num_of_20 = 0
        num_of_5 = 0
        num_of_10 = 0
    def lemonadeChange(self, bills: List[int]) -> bool:
[
