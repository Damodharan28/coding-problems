class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize a pointer for iterating through the strings
        p1 = 0
        # Get the lengths of both input strings
        size1 = len(word1)
        size2 = len(word2)
        # Initialize the result string
        res = ""

        # Loop until the pointer exceeds the length of both strings
        while p1 < size1 or p1 < size2:
            # If the pointer is within the bounds of the first string, add the character to the result
            if p1 < size1:
                res = res + word1[p1]
            # If the pointer is within the bounds of the second string, add the character to the result
            if p1 < size2:
                res = res + word2[p1]
            # Increment the pointer
            p1 += 1

        # Return the merged result string
        return res
