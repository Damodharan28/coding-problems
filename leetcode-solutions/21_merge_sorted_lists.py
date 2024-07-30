class Solution:
    def mergeTwoLists(self, list1, list2):
        # If list1 is empty, return list2 as the merged result
        if not list1:
            return list2
        
        # If list2 is empty, return list1 as the merged result
        if not list2:
            return list1
        
        # Ensure list1 starts with the smaller value for easier merging
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        # Initialize the head of the merged list to be the smaller of the two starting nodes
        head = list1
        
        # Traverse both lists until we reach the end of one of them
        while list1 and list2:
            # Keep track of the last node in the merged list
            prev = None
            
            # Move through list1 until finding a node with a value greater than list2's current node
            while list1 and list1.val <= list2.val:
                prev = list1
                list1 = list1.next
            
            # Link the remaining part of list2 to the end of list1's current position
            prev.next = list2
            
            # Swap list1 and list2 for the next iteration
            list1, list2 = list2, list1

        return head
