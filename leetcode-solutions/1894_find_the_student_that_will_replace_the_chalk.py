class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)

        rem = k % total 
        if rem == 0: return 0
        for i in range(len(chalk)):
            rem = rem - chalk[i]
            if rem < 0 : return i
