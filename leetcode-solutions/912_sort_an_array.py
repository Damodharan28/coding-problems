class Solution(object):
    def sortArray(self, nums):
        # Function to merge two halves of an array
        def merge(arr, begin, mid, end):
            # Create temporary arrays for left and right halves
            left_arr = arr[begin : mid+1]
            right_arr = arr[mid+1: end+1]

            # Get the sizes of the left and right arrays
            l_size = len(left_arr)
            r_size = len(right_arr)

            # Initialize indices for left, right, and sorted portions of the array
            left_index = 0
            right_index = 0
            sorted_index = begin

            # Merge the temporary arrays back into the original array
            while left_index < l_size and right_index < r_size:
                if left_arr[left_index] <= right_arr[right_index]:
                    arr[sorted_index] = left_arr[left_index]
                    left_index += 1
                else:
                    arr[sorted_index] = right_arr[right_index]
                    right_index += 1
                sorted_index += 1

            # Copy any remaining elements of left_arr, if any
            while left_index < l_size:
                arr[sorted_index] = left_arr[left_index]
                left_index += 1
                sorted_index += 1

            # Copy any remaining elements of right_arr, if any
            while right_index < r_size:
                arr[sorted_index] = right_arr[right_index]
                right_index += 1
                sorted_index += 1

        # Function to implement the merge sort algorithm
        def mergesort(arr, begin, end):
            # Base case: if the array has one or no elements
            if begin >= end:
                return 
            
            # Find the midpoint of the array
            mid = begin + (end - begin) // 2
            
            # Recursively sort the first half
            mergesort(arr, begin, mid)
            
            # Recursively sort the second half
            mergesort(arr, mid + 1, end)
            
            # Merge the two sorted halves
            merge(arr, begin, mid, end)

        # Call the mergesort function on the entire array
        mergesort(nums, 0, len(nums) - 1)
        return nums
