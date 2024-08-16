class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn = arrays[0][0]
        mx = arrays[0][-1]
        mx_dist = 0

        for i in range(1,len(arrays)):
            arr = arrays[i]
            mx_dist = max(mx_dist, abs(arr[-1] - mn), abs(mx - arr[0]))
            mn = min(mn, arr[0])
            mx = max(mx, arr[-1])

        return mx_dist
