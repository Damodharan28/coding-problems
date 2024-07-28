from collections import defaultdict
import heapq

class Solution:
    def secondMinimum(self, n, edges, time, change):
        # Create an adjacency list representation of the graph
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # Priority queue to hold (time, node) tuples
        q = []
        heapq.heappush(q, (0, 1))  # Start with node 1 at time 0
        
        # Arrays to track the number of visits and the first and second times each node is reached
        visit_count = [0] * (n + 1)
        first_time = [-1] * (n + 1)
        second_time = [-1] * (n + 1)
        
        while q:
            t, node = heapq.heappop(q)  # Get the node with the smallest time
            
            # Skip processing if we've already recorded this time or visited the node twice
            if first_time[node] == t or second_time[node] == t or visit_count[node] >= 2:
                continue
            
            # Increment the visit count for the node
            visit_count[node] += 1
            
            # Record the first and second times the node is reached
            if visit_count[node] == 1:
                first_time[node] = t
            else:
                second_time[node] = t
            
            # If we've reached the target node (n) for the second time, return the second time
            if node == n and visit_count[node] == 2:
                return second_time[node]
            
            # If we're in a red light period, wait until the green light
            if (t // change) % 2 != 0:
                t = (t // change + 1) * change
            
            # Push all neighbors into the priority queue with updated times
            for nei in g[node]:
                heapq.heappush(q, (t + time, nei))
        
        return -1 
