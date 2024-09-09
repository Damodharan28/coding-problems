# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1]*n for _ in range(m)]
        direct = [(0,1),(1,0),(0,-1),(-1,0)]
        d = 0
        curr = head
        i,j = 0,0
        while curr:
            res[i][j] = curr.val
            curr = curr.next
            next_i , next_j = i + direct[d%4][0] , j + direct[d%4][1]

            if 0 <= next_i < m and 0 <= next_j < n and res[next_i][next_j]==-1:
                i,j = next_i, next_j
            else:
                d += 1
                i,j = i + direct[d%4][0] , j + direct[d%4][1]

        return res
