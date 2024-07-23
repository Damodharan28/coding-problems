class Solution:
    def frequencySort(self, nums):
        # Initialize frequency array
        freq = [0] * 201  # We use 201 to cover the range from -100 to 100

        # Count frequencies of each number
        for x in nums:
            freq[x + 100] -= 1  # Increment the frequency count

        # Sort the numbers based on frequency and value
        sorted_nums = sorted(nums, key=lambda x: (freq[x + 100], x), reverse=True)
        return sorted_nums

solution = Solution()
nums = [1,1,2,2,2,3]
solution.frequencySort(nums)
