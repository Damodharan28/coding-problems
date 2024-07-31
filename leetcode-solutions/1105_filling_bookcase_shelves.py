class Solution:
    def minHeightShelves(self, books, shelfWidth):
        # Number of books
        n = len(books)  
        # Initialize dp array with infinity
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  

        # Iterate over each book
        for i in range(1, n + 1):
            width = 0  # Initialize current shelf width
            height = 0  # Initialize current shelf height
          
            # Iterate backwards to consider placing books from j to i on the same shelf
            for j in range(i, 0, -1):
                 # Add the thickness of book[j-1] to the current shelf width
                width += books[j - 1][0]
              
                if width > shelfWidth:  # If the current shelf width exceeds shelfWidth, break
                    break
                  
                # Update the shelf height to the maximum height of books placed on it
                height = max(height, books[j - 1][1])
                # Update dp[i] with the minimum height
                dp[i] = min(dp[i], dp[j - 1] + height)  

        return dp[n]
