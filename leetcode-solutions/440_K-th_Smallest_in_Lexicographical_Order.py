class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        while k > 0:
            cnt = self.countPrefix(curr,n)
            if k >= cnt:
                curr += 1
                k -= cnt
            else:
                curr *= 10
                k -= 1
        
        return curr
    
    def countPrefix(self,prefix,n):
        f_num = prefix
        n_num = prefix + 1
        total_cnt = 0

        while f_num <= n :
            total_cnt += min(n+1, n_num) - f_num
            f_num *= 10
            n_num *= 10

        return total_cnt
