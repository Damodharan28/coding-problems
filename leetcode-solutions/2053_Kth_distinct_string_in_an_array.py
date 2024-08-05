class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Sets to keep track of distinct and non-distinct words
        distinct = set()     # Holds words that have appeared only once so far
        nonDistinct = set()  # Holds words that have appeared more than once
        
        # Iterate through the array to classify words as distinct or non-distinct
        for word in arr:
            # If the word is not in the non-distinct set
            if word not in nonDistinct:
                # If the word is already in the distinct set
                if word in distinct:
                    # Move the word from distinct set to non-distinct set
                    distinct.remove(word)
                    nonDistinct.add(word)
                else:
                    # Otherwise, add the word to the distinct set
                    distinct.add(word)
        
        # If there are fewer distinct words than k, return an empty string
        if len(distinct) < k:
            return ""
        
        # Iterate through the array again to find the k-th distinct word
        for word in arr:
            # If the word is in the distinct set
            if word in distinct:
                k -= 1  # Decrease k by 1
                # When k becomes 0, return the current word
                if k == 0:
                    return word
        
        # If no k-th distinct word is found, return an empty string
        return ""
