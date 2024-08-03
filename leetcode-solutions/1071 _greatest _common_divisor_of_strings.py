from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenating the strings in both orders produces the same result.
        # If not, there is no common divisor string.
        if str1 + str2 != str2 + str1:
            return ""
        
        # Calculate the greatest common divisor of the lengths of the two strings.
        gcd_length = gcd(len(str1), len(str2))
        
        # The greatest common divisor string will be the prefix of str1 up to the gcd length.
        return str1[:gcd_length]
