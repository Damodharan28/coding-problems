class Solution(object):
    def sortJumbled(self, mapping, nums):
        # Function to map the digits of a number according to the given mapping
        def map_value(num):
            # Convert the number to a string to process each digit
            temp = str(num)
            val = ""
            # Replace each digit with the corresponding mapped value
            for ch in temp:
                val += str(mapping[int(ch)])
            # Convert the mapped value back to an integer and return it
            return int(val)

        # Sort the nums array based on the mapped values
        nums.sort(key=map_value)
        return nums


solution = Solution()
mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]
print(solution.sortJumbled(mapping, nums))
