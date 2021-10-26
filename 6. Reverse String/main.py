class Solution:
    def reverseString(self, s: List[str]) -> None:
        mid = len(s)//2
        temp = None
        for i in range(mid):
            temp = s[i]
            print(len(s)-(i+1))
            s[i] = s[len(s)-(i+1)]
            s[len(s)-(i+1)] = temp
            
