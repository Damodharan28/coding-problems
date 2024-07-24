class Solution(object):
    def twoSum(self, nums, target):
        # Get the number of elements in nums
        size = len(nums)
        
        # Loop through each element in nums except the last one
        for i in range(size - 1):
            # For each element nums[i], loop through the elements that come after it
            for j in range(i + 1, size):
                # Check if the sum of nums[i] and nums[j] equals the target
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # If no such pair is found, return an empty list
        return []

solution = Solution()
nums = [2, 7, 11, 15]
target = 9
solution.twoSum(nums, target)
