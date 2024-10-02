class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranking = {}
        sorted_arr = sorted(set(arr))

        for i in range(len(sorted_arr)):
            ranking[sorted_arr[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = ranking[arr[i]]

        return arr
