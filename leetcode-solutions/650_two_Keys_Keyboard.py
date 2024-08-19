class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        opt = 0
        factor = 2
        
        while n > 1:
            while n % factor == 0:
                opt += factor
                n //= factor
            factor += 1
            
        return opt
