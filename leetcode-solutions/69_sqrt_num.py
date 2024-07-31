class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        
        left, right = 1, x
        result = 0
        # binary search approach
        while left <= right:
            mid = (left + right) // 2  # Find the middle point
            mid_squared = mid * mid  # Calculate mid squared
            
            if mid_squared == x:  # If mid squared is exactly x, mid is the square root
                return mid
            elif mid_squared < x:  # If mid squared is less than x, update result and move to the right half
                result = mid
                left = mid + 1
            else:  # If mid squared is greater than x, move to the left half
                right = mid - 1
        
        return result
