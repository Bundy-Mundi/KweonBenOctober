class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        CONST = 64
        total = 0
        digit = 0
        for i in range(len(columnTitle)-1, -1, -1):
            num = ord(columnTitle[i]) - CONST
            total += num*math.pow(26, digit)
            digit += 1
        return int(total)
        
