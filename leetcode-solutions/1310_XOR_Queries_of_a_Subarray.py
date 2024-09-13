class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        arr[:] = accumulate(arr,xor)
        res = [0] * len(queries)

        for i,(q0, qn) in enumerate(queries):
            if q0 == 0:
                res[i] = arr[qn]
            else:
                res[i] = arr[qn]^arr[q0-1]

        return res
