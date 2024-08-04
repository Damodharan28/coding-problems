class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = "aeiouAEIOU"
        
        while left < right:
            while left < right and vowels.find(s[left]) == -1:
                left += 1
            while left < right and vowels.find(s[right]) == -1:
                right -= 1
            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return "".join(s)
