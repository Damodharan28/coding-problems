class Solution:
    def frequencySort(self, nums):
        freq=[0]*201
        for x in nums:
            freq[x+100]-=1 
        return sorted(nums, key=lambda x:(freq[x+100], x), reverse=True)


sol = Solution()
nums = [1,1,2,2,2,3]
sol.frequencySort(nums)