class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(str(x)[::-1])
        x = list(str(x))
        result = 0
        for i in range(len(x)):
            
            if(x[i]==y[i]):
                continue
            else:
                result = 1
        if(result==1):
            return False
        else:
            return True

        
