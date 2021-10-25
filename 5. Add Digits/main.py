import math
class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        digits = 1
        if num != 0: digits = math.ceil(math.log(num,10))
        if num < 10: return num
        for i in range(0, digits+1):
            total += num%10
            num = num//10  
        return self.addDigits(total)
