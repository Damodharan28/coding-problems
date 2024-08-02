class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Count the total number of 1's in the list
        k = nums.count(1)
        
        # Calculate the number of 1's in the initial window of size k
        mx = cnt = sum(nums[:k])
        
        # Get the length of the list
        n = len(nums)
        
        # Use a sliding window to find the maximum number of 1's in any window of size k
        for i in range(k, n + k):
            # Add the next element in the circular manner
            cnt += nums[i % n]
            
            # Remove the element that is no longer in the window
            cnt -= nums[(i - k + n) % n]
            
            # Update the maximum number of 1's found in any window of size k
            mx = max(mx, cnt)
        
        # The minimum number of swaps needed is the total number of 1's minus
        # the maximum number of 1's in any window of size k
        return k - mx
